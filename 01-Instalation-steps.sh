# Depoly docker compose plugin
sudo apt-get install docker-compose-plugin
# Deploy Hasicorp Vault for Secrets Management
docker run -p 8200:8200 -e 'VAULT_DEV_ROOT_TOKEN_ID=dev-only-token' vault

# Create data structure for Fishy Tank
mkdir -p /opt/fishy-auto/postgres/data/
mkdir -p /opt/fishy-auto/docker/secrets

# Create Secrets Files in docker
docker secret create /opt/fishy-auto/postgres/data/fishy.secrets

# Deploy postgresSQL container 
cd ./postgres/
docker compose up
