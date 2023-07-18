import psycopg2

# Define variables
db_name = 'fishydb'  # Set this to the actual target database name
user_name = 'fishy_user'
user_password = 'D0gmat1x'

# Connect to the PostgreSQL server
try:
    connection = psycopg2.connect(
        host='localhost',
        port=15432,
        user=user_name,
        password=user_password,
        dbname=db_name
    )
    cursor = connection.cursor()
except Exception as e:
    print(f"Error connecting to database: {e}")
    exit(1)

# Create ENUM types
enums = {
    "origin": """
    DO $$ BEGIN
        CREATE TYPE origin AS ENUM ('African Rivers', 'Asian Rivers', 'Indian Rivers', 'Australian Rivers', 'South American Rivers', 'Central American Rivers', 'Central American Lakes', 'African Lakes', 'Mangrove Forests');
    EXCEPTION
        WHEN duplicate_object THEN null;
    END $$;
    """,
    "difficulty": """
    DO $$ BEGIN
        CREATE TYPE difficulty AS ENUM ('Beginner', 'Intermediate', 'Experienced', 'Expert');
    EXCEPTION
        WHEN duplicate_object THEN null;
    END $$;
    """,
    "availability": """
    DO $$ BEGIN
        CREATE TYPE availability AS ENUM ('Very Common', 'Common', 'Uncommon', 'Rare');
    EXCEPTION
        WHEN duplicate_object THEN null;
    END $$;
    """
}

for enum_name, enum_definition in enums.items():
    try:
        cursor.execute(enum_definition)
        print(f"ENUM '{enum_name}' created successfully.")
    except Exception as e:
        print(f"Error creating ENUM '{enum_name}': {e}")

cursor = connection.cursor()

# Create the tables
tables = {
    "Aquarium": """
    CREATE TABLE IF NOT EXISTS Aquarium (
        AqId SERIAL PRIMARY KEY,
        name VARCHAR(255),
        depth FLOAT,
        width FLOAT,
        height FLOAT,
        waterVolume FLOAT,
        type VARCHAR(255),
        startDate VARCHAR(255),
        endDate VARCHAR(255),
        newStartDate DATE,
        newEndDate DATE,
        open BOOL,
        imagePresent BOOL,
        aquariumImage BYTEA,
        tankVolume FLOAT,
        bottom FLOAT,
        glassThick FLOAT,
        notes VARCHAR(255),
        waterChange FLOAT
    )
    """,
    "Device": """
    CREATE TABLE IF NOT EXISTS Device (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        brand VARCHAR(255),
        wattage FLOAT,
        notes VARCHAR(255),
        onPeriod VARCHAR(255),
        qty INT,
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
    )
    """,
    "Expense": """
    CREATE TABLE IF NOT EXISTS Expense (
        id SERIAL PRIMARY KEY,
        date VARCHAR(255),
        item VARCHAR(255),
        price FLOAT,
        notes VARCHAR(255),
        shop VARCHAR(255),
        type VARCHAR(255),
        newDate DATE,
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
    )
    """,
    "History": """
    CREATE TABLE IF NOT EXISTS History (
        id SERIAL PRIMARY KEY,
        date VARCHAR(255),
        time VARCHAR(255),
        event VARCHAR(255),
        newDate DATE,
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
    )
    """,
    "Maintenance": """
    CREATE TABLE IF NOT EXISTS Maintenance (
        id SERIAL PRIMARY KEY,
        date VARCHAR(255),
        time VARCHAR(255),
        event VARCHAR(255),
        units VARCHAR(255),
        notes VARCHAR(255),
        warnings VARCHAR(255),
        newDate DATE,
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
    )
    """,
    "Plans": """
    CREATE TABLE IF NOT EXISTS Plans (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        method VARCHAR(255),
        recipe VARCHAR(255),
        fertInterval INT,
        fertDelay INT,
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
    )
    """,
    "Reading": """
    CREATE TABLE IF NOT EXISTS Reading (
        id SERIAL PRIMARY KEY,
        date VARCHAR(255),
        time VARCHAR(255),
        no2 FLOAT,
        no3 FLOAT,
        gh FLOAT,
        kh FLOAT,
        ph FLOAT,
        temp FLOAT,
        fe FLOAT,
        nh FLOAT,
        co2 FLOAT,
        cond FLOAT,
        ca FLOAT,
        mg FLOAT,
        cu FLOAT,
        newDate DATE,
        po4 FLOAT,
        o2 FLOAT,
        dens FLOAT,
        nh3 FLOAT,
        iodine FLOAT,
        salinity FLOAT,
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
    )
    """,
    "Recipe": """
    CREATE TABLE IF NOT EXISTS Recipe (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        notes VARCHAR(255),
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
    )
    """,
    "Test": """
    CREATE TABLE IF NOT EXISTS Test (
        id SERIAL PRIMARY KEY,
        date VARCHAR(255),
        time VARCHAR(255),
        notes VARCHAR(255),
        newDate DATE,
        nh3 FLOAT,
        no2 FLOAT,
        no3 FLOAT,
        ph FLOAT,
        kh FLOAT,
        gh FLOAT,
        po4 FLOAT,
        fe FLOAT,
        cu FLOAT,
        o2 FLOAT,
        co2 FLOAT,
        ca FLOAT,
        mg FLOAT,
        cond FLOAT,
        temp FLOAT,
        dens FLOAT,
        tds FLOAT,
        salinity FLOAT,
        orp FLOAT,
        nh4 FLOAT,
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
    )
    """,
    "Treatment": """
    CREATE TABLE IF NOT EXISTS Treatment (
        id SERIAL PRIMARY KEY,
        date VARCHAR(255),
        notes VARCHAR(255),
        newDate DATE,
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
    )
    """,
    "Chemical": """
    CREATE TABLE IF NOT EXISTS Chemical (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
    )
    """,
    "Fish": """
    CREATE TABLE IF NOT EXISTS Fish (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
    )
    """,
    "Food": """
    CREATE TABLE IF NOT EXISTS Food (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
    )
    """,
    "Plant": """
    CREATE TABLE IF NOT EXISTS Plant (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
    )
    """,
    "Inhabitant": """
    CREATE TABLE IF NOT EXISTS Inhabitant (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        qty INT,
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
    )
    """,
    "Brand": """
    CREATE TABLE IF NOT EXISTS Brand (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        website VARCHAR(255),
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
    )
    """,
    "FishStore": """
    CREATE TABLE IF NOT EXISTS FishStore (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        location VARCHAR(255),
        website VARCHAR(255),
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
    )
    """,
    "Fishbase": """
    CREATE TABLE IF NOT EXISTS Fish (
        fish_id SERIAL PRIMARY KEY,
        common_name VARCHAR(255),
        scientific_name VARCHAR(255),
        family VARCHAR(255),
        origin origin,
        size FLOAT,
        tank_size INT,
        temperature_range VARCHAR(255),
        ph_range VARCHAR(255),
        temperament VARCHAR(255),
        difficulty difficulty,
        min_tank_size INT,
        adult_size FLOAT,
        min_ph FLOAT,
        max_ph FLOAT,
        min_temperature FLOAT,
        max_temperature FLOAT,
        min_carbonate_hardness INT,
        max_carbonate_hardness INT,
        min_general_hardness INT,
        max_general_hardness INT,
        stocking_ratio VARCHAR(255),
        availability availability,
        diet VARCHAR(255),
        lifespan INT,
        habitat VARCHAR(255),
        sexing VARCHAR(255),
        breeding VARCHAR(255),
        tank_compatibility VARCHAR(255),
        diet_extended VARCHAR(255),
        feeding_regime VARCHAR(255),
        environmental_specifics VARCHAR(255),
        behaviour VARCHAR(255),
        identification VARCHAR(255),
        species_note VARCHAR(255),
        pictures TEXT,
        AqId INT,
        FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
        )
        """,
        "Plants": """
        CREATE TABLE IF NOT EXISTS Plants (
            plant_id SERIAL PRIMARY KEY,
            common_name VARCHAR(255),
            scientific_name VARCHAR(255),
            family VARCHAR(255),
            origin VARCHAR(255),
            growth_rate VARCHAR(255),
            light_requirements VARCHAR(255),
            co2_requirements VARCHAR(255),
            substrate VARCHAR(255),
            propagation VARCHAR(255),
            AqId INT,
            FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
        )
        """,
        "Invertebrates": """
        CREATE TABLE IF NOT EXISTS Invertebrates (
            invertebrate_id SERIAL PRIMARY KEY,
            common_name VARCHAR(255),
            scientific_name VARCHAR(255),
            family VARCHAR(255),
            origin VARCHAR(255),
            size FLOAT,
            tank_size INT,
            temperature_range VARCHAR(255),
            ph_range VARCHAR(255),
            diet VARCHAR(255),
            AqId INT,
            FOREIGN KEY (AqId) REFERENCES Aquarium(AqId)
        )
        """
            
        }

for table_name, table_definition in tables.items():
    try:
        cursor.execute(table_definition)
        print(f"Table '{table_name}' created successfully.")
    except Exception as e:
        print(f"Error creating table '{table_name}': {e}")

# Commit the changes
connection.commit()

cursor.close()
connection.close()

