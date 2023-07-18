#!/bin/bash

# Functions
check_file_exist() {
    if [ ! -f "$1" ]; then
        echo "$1 not found in the current directory."
        exit 1
    fi
}

remove_docker_entity() {
    local ENTITY=$1
    local NAME=$2
    local TYPE=$3
    if [ "$(docker ${ENTITY} -q -f name=$NAME)" ]; then
        echo "Docker ${TYPE} already exists. Stopping and Removing..."
        docker $TYPE rm $NAME
        sleep 2
        if [ "$(docker ${ENTITY} -q -f name=$NAME)" ]; then
            echo "Failed to stop and remove existing Docker ${TYPE}."
            exit 1
        fi
    fi
}

# Set Variables
CONTAINER_NAME="Fishy-App_psql"
IMAGE_NAME="fishy-app_psql"
NEW_USER="fishy_user"
NEW_PASSWORD="D0gmat1x"
TARGET_DB="fishydb"
POSTGRES_USER_PASSWORD="Aster1x"

# Check if Dockerfile and Python script exist in the current directory
check_file_exist "Dockerfile"
check_file_exist "fishy-create-psql-db.py"

# Check if the Docker container already exists
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "Docker container already exists. Stopping..."
    docker stop $CONTAINER_NAME
    if [ $? -ne 0 ]; then
        echo "Failed to stop existing Docker container."
        exit 1
    fi

    echo "Removing Docker container..."
    docker rm $CONTAINER_NAME
    if [ $? -ne 0 ]; then
        echo "Failed to remove existing Docker container."
        exit 1
    fi
fi

# Check if the Docker container and image already exists
remove_docker_entity "ps" "$CONTAINER_NAME" "container"
remove_docker_entity "images" "$IMAGE_NAME" "image"

# Build Docker image
echo "Building Docker image..."
docker build -t $IMAGE_NAME .
if [ $? -ne 0 ]; then
    echo "Failed to build Docker image."
    exit 1
fi

# Wait for Docker image to be ready
echo "Waiting for Docker image to be ready..."
for i in {1..10}; do
    if [ "$(docker images -q $IMAGE_NAME)" ]; then
        echo "Docker image is ready."
        break
    elif [ $i -eq 10 ]; then
        echo "Docker image did not become ready in time. Exiting..."
        exit 1
    else
        echo "Docker image is not ready, retrying..."
        sleep 5
    fi
done

# Deploy PostgreSQL container
echo "Deploying PostgreSQL container..."
docker run --name $CONTAINER_NAME -p 15432:5432 -e POSTGRES_PASSWORD=$POSTGRES_USER_PASSWORD -d $IMAGE_NAME
if [ $? -ne 0 ]; then
    echo "Failed to deploy PostgreSQL container."
    exit 1
fi

# Wait for PostgreSQL service to become ready
echo "Waiting for PostgreSQL service to become ready..."
for i in {1..10}; do
    docker exec -it $CONTAINER_NAME pg_isready -U postgres
    if [ $? -eq 0 ]; then
        echo "PostgreSQL is ready."
        break
    elif [ $i -eq 10 ]; then
        echo "PostgreSQL service did not become ready in time. Exiting..."
        exit 1
    else
        echo "PostgreSQL is not ready, retrying..."
        sleep 5
    fi
done

# Create a new user with createdb privileges
echo "Creating a new user..."
if [ "$(docker exec $CONTAINER_NAME psql -U postgres -tAc "SELECT 1 FROM pg_roles WHERE rolname='$NEW_USER'")" != '1' ]; then
    echo "Creating new PostgreSQL role..."
    docker exec $CONTAINER_NAME psql -U postgres -c "CREATE ROLE $NEW_USER LOGIN PASSWORD '$NEW_PASSWORD';"
    if [ $? -ne 0 ]; then
        echo "Failed to create a new user."
        exit 1
    else
        echo "New user created successfully."
    fi
else
    echo "User already exists."
fi

# Check if the new user was created
echo "Checking if the new user was created..."
if [ "$(docker exec $CONTAINER_NAME psql -U postgres -tAc "SELECT 1 FROM pg_roles WHERE rolname='$NEW_USER'")" != '1' ]; then
    echo "Failed to verify the creation of the new user."
    exit 1
fi

echo "Checking if the new user can create databases..."
CAN_CREATE_DB=$(docker exec -i $CONTAINER_NAME psql -U postgres -c "SELECT rolcreatedb FROM pg_roles WHERE rolname='$NEW_USER';" | grep -o 't')
if [[ "$CAN_CREATE_DB" != "t" ]]; then
    echo "User cannot create databases. Assigning the CREATEDB privilege..."
    OUTPUT=$(docker exec -it $CONTAINER_NAME psql -U postgres -c "ALTER USER $NEW_USER CREATEDB;")
    if [[ $? -ne 0 ]]; then
        echo "Failed to assign the CREATEDB privilege."
        echo "Error: $OUTPUT"
        exit 1
    fi
    echo "CREATEDB privilege assigned successfully."
fi

# Check again if the new user can create databases
CAN_CREATE_DB=$(docker exec -i $CONTAINER_NAME psql -U postgres -c "SELECT rolcreatedb FROM pg_roles WHERE rolname='$NEW_USER';" | grep -o 't')
if [[ "$CAN_CREATE_DB" != "t" ]]; then
    echo "Failed to assign the CREATEDB privilege."
    exit 1
fi
echo "New user can create databases."

# Create the database
echo "Creating the target database..."
docker exec -i $CONTAINER_NAME psql -U postgres -c "CREATE DATABASE $TARGET_DB;"
if [ $? -ne 0 ]; then
    echo "Failed to create the target database."
    exit 1
fi

# Grant permissions to the new user
echo "Granting all privileges to new user on the public schema..."
docker exec -i $CONTAINER_NAME psql -U postgres -d $TARGET_DB -c "GRANT ALL PRIVILEGES ON SCHEMA public TO $NEW_USER;"
if [ $? -ne 0 ]; then
    echo "Failed to grant privileges to the new user."
    exit 1
fi

# Disconnect all other users
echo "Disconnecting all other users..."
docker exec $CONTAINER_NAME psql -U postgres <<EOSQL
SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = '$TARGET_DB' AND pid <> pg_backend_pid();
EOSQL
if [ $? -ne 0 ]; then
    echo "Failed to disconnect all other users."
    exit 1
fi

# Run the Python script
echo "Running Python script..."
python3 fishy-create-psql-db.py
if [ $? -ne 0 ]; then
    echo "Failed to run the Python script."
    exit 1
fi

echo "Done."