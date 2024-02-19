import sqlite3

# Connect to the database (will create it if it doesn't exist)
conn = sqlite3.connect('Fishy_v_02.db')
cursor = conn.cursor()

# Create tables
tables = [
    """
    CREATE TABLE Supplier (
        supplier_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        contact_person TEXT,
        phone_number TEXT,
        alternate_phone_number TEXT,
        email TEXT,
        address TEXT,
        city TEXT,
        state_province TEXT,
        country TEXT,
        postal_code TEXT,
        website TEXT,
        notes TEXT
    )
    """,
    """
    CREATE TABLE Aquarium (
        id INTEGER PRIMARY KEY,
        name TEXT,
        tank_type TEXT CHECK(tank_type IN ('breeding', 'community', 'quarantine', 'species')),
        water_type TEXT CHECK(water_type IN ('Freshwater', 'Saltwater', 'Brackish water')),
        shape TEXT CHECK(shape IN ('Cube', 'Rectangular', 'Bow-front', 'Bevelled-front', 'Other')),
        length_cm REAL,
        width_cm REAL,
        depth_cm REAL,
        capacity_liters REAL,
        substrate TEXT CHECK(substrate IN ('None', 'Gravel', 'Sand', 'Aqua Soil', 'Pebbles')),
        commissioned_date DATE,
        decommissioned_date DATE,
        price_euro REAL,
        vendor_id INTEGER,
        equipment TEXT CHECK(equipment IN ('Filters', 'Lights', 'Pumps', 'Heaters', 'Others')),
        co2 TEXT CHECK(co2 IN ('Yes', 'No')),
        target_co2_ppm REAL,
        target_temp_c REAL,
        target_ph REAL,
        target_kh_ppm REAL,
        target_gh_ppm REAL,
        notes TEXT,
        FOREIGN KEY (vendor_id) REFERENCES Supplier(supplier_id)
    )
    """,
    """
    CREATE TABLE Images (
        image_id INTEGER PRIMARY KEY,
        entity_type TEXT CHECK(entity_type IN ('Fish', 'Invertebrate', 'Plant', 'Aquarium', 'Equipment')),
        entity_id INTEGER,
        image BLOB
    )
    """,
    """
    CREATE TABLE TankMates (
        id INTEGER PRIMARY KEY,
        fish_id INTEGER,
        mate_name TEXT,
        FOREIGN KEY (fish_id) REFERENCES Fish(id)
    )
    """,
    """
    CREATE TABLE Fish (
        id INTEGER PRIMARY KEY,
        size TEXT,
        aquarium_id INTEGER,
        supplier_id INTEGER,
        scientific_name TEXT,
        common_names TEXT,
        care_level TEXT CHECK(care_level IN ('Beginner', 'Intermediate', 'Experienced', 'Expert')),
        tank_region TEXT CHECK(tank_region IN ('Bottom', 'Bottom and Middle', 'Middle', 'Middle and Top', 'Top', 'All Ranges')),
        tank_region_summary TEXT,
        size_cm REAL,
        ph_min REAL,
        ph_max REAL,
        temp_min REAL,
        temp_max REAL,
        gh_min REAL,
        gh_max REAL,
        kh_min REAL,
        kh_max REAL,
        origin_habitat TEXT CHECK(origin_habitat IN ('African River', 'Asian River', 'Indian River', 'South American River', 'Central American River', 'Central American Lake', 'African Lakes', 'Mangrove Forest', 'Australian River', 'Worldwide')),
        lifespan_years REAL,
        social_behavior TEXT CHECK(social_behavior IN ('Peaceful', 'Tolerant', 'Gregarious', 'Aggressive', 'Territorial', 'Fin Nipper', 'Solitary')),
        breeding TEXT,
        min_aquarium_size REAL,
        diet_food TEXT CHECK(diet_food IN ('Carnivore', 'Herbivore', 'Limnivore', 'Omnivore')),
        diet_summary TEXT,
        gender_descriptions TEXT,
        synopsis TEXT,
        notes TEXT,
        FOREIGN KEY (aquarium_id) REFERENCES Aquarium(id),
        FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id)
    )
    """,
    """
    CREATE TABLE Equipment (
        id INTEGER PRIMARY KEY,
        type TEXT,
        brand TEXT,
        supplier_id INTEGER,
        aquarium_id INTEGER,
        qty_per_type INTEGER,
        active TEXT CHECK(active IN ("Yes", "No")),
        model TEXT,
        purchase_date DATE,
        setup_date DATE,
        unit_price REAL,
        performance_lph REAL,
        power_input TEXT CHECK(power_input IN ("220v", "110v")),
        power_consumption REAL,
        run_time_hrs_per_day REAL,
        maintenance_interval_days INTEGER,
        replacement_interval_days INTEGER,
        notes TEXT,
        FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id),
        FOREIGN KEY (aquarium_id) REFERENCES Aquarium(id)
    )
    """,
    """
    CREATE TABLE Invertebrate (
        id INTEGER PRIMARY KEY,
        size TEXT,
        aquarium_id INTEGER,
        supplier_id INTEGER,
        common_names TEXT,
        scientific_name TEXT,
        care_level TEXT CHECK(care_level IN ('Beginner', 'Intermediate', 'Experienced', 'Expert')),
        size_min_cm REAL,
        size_max_cm REAL,
        ph_min REAL,
        ph_max REAL,
        temperature_min_c REAL,
        temperature_max_c REAL,
        water_hardness_gh_min REAL,
        water_hardness_gh_max REAL,
        water_hardness_kh_min REAL,
        water_hardness_kh_max REAL,
        origin_habitat TEXT CHECK(origin_habitat IN ('African River', 'Asian River', 'Indian River', 'South American River', 'Central American River', 'Central American Lake', 'African Lakes', 'Mangrove Forest', 'Australian River', 'Worldwide')),
        social_behavior TEXT CHECK(social_behavior IN ('Peaceful', 'Tolerant', 'Gregarious', 'Aggressive', 'Territorial', 'Fin Nipper', 'Solitary')),
        diet_food TEXT CHECK(diet_food IN ('Carnivore', 'Herbivore', 'Limnivore', 'Omnivore')),
        diet_summary TEXT,
        gender_descriptions TEXT,
        synopsis TEXT,
        notes TEXT,
        FOREIGN KEY (aquarium_id) REFERENCES Aquarium(id),
        FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id)
    )
    """,
    """
    CREATE TABLE Plant (
        id INTEGER PRIMARY KEY,
        size TEXT,
        aquarium_id INTEGER,
        supplier_id INTEGER,
        region TEXT CHECK(region IN ('Asia', 'Africa', 'Europe', 'North America', 'South America', 'Australia', 'Cosmopolitan', 'Cultivar')),
        type TEXT CHECK(type IN ('Bulb/Onion', 'Carpeting', 'Moss', 'Rhizome', 'Rosette', 'Stem', 'Stolon')),
        placement TEXT CHECK(placement IN ('Foreground', 'Midground', 'Background')),
        growth_rate TEXT CHECK(growth_rate IN ('Slow', 'Medium', 'Fast')),
        light_requirement TEXT CHECK(light_requirement IN ('Low', 'Medium', 'High')),
        co2_requirement TEXT CHECK(co2_requirement IN ('Low', 'Medium', 'High')),
        ph_min REAL,
        ph_max REAL,
        temperature_min_c REAL,
        temperature_max_c REAL,
        water_hardness_gh_min REAL,
        water_hardness_gh_max REAL,
        water_hardness_kh_min REAL,
        water_hardness_kh_max REAL,
        notes TEXT,
        FOREIGN KEY (aquarium_id) REFERENCES Aquarium(id),
        FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id)
    )
    """,
    """
    CREATE TABLE WaterParameter (
        id INTEGER PRIMARY KEY,
        aquarium_id INTEGER,
        date DATE,
        ph REAL,
        kh REAL,
        gh REAL,
        ammonia_ppm REAL,
        nitrite_ppm REAL,
        nitrate_ppm REAL,
        phosphate_ppm REAL,
        calcium_ppm REAL,
        magnesium_ppm REAL,
        potassium_ppm REAL,
        iron_ppm REAL,
        tds_ppm REAL,
        temperature_c REAL,
        notes TEXT,
        FOREIGN KEY (aquarium_id) REFERENCES Aquarium(id)
    )
    """,
    """
    CREATE TABLE SupplierProducts (
        id INTEGER PRIMARY KEY,
        supplier_id INTEGER,
        product_name TEXT,
        product_type TEXT,
        product_description TEXT,
        price REAL,
        FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id)
    )
    """,
    """
    CREATE TABLE MaintenanceTask (
        task_id INTEGER PRIMARY KEY,
        aquarium_id INTEGER,
        task_name TEXT CHECK(task_name IN ('Water Change', 'Vacumn gravel', 'Filter media change', 'Air stone change', 'Clean heater body', 'Clean filter body & impeller', 'Clean decorations')),
        task_description TEXT,
        task_frequency_value INTEGER,
        task_frequency_unit TEXT CHECK(task_frequency_unit IN ('days', 'weeks', 'months')),
        last_performed DATE,
        next_scheduled DATE,
        FOREIGN KEY (aquarium_id) REFERENCES Aquarium(id)
    )
    """,
    """
    CREATE TABLE TaskList (
        task_id INTEGER PRIMARY KEY,
        task_name TEXT NOT NULL UNIQUE
    )
    """,
    """
    CREATE TABLE Versioning (
        version_id INTEGER PRIMARY KEY,
        version_name TEXT NOT NULL,
        version_date DATE DEFAULT CURRENT_DATE
    )
    """,
    """
    CREATE TABLE Inventory (
        inventory_id INTEGER PRIMARY KEY,
        aquarium_id INTEGER,
        entity_type TEXT CHECK(entity_type IN ('Fish', 'Plant', 'Invertebrate', 'TankMates', 'Equipment')),
        entity_id INTEGER,
        date_added DATE DEFAULT CURRENT_DATE,
        FOREIGN KEY (aquarium_id) REFERENCES Aquarium(id)
    )
    """
]

for table in tables:
    cursor.execute(table)

# Insert the initial version
cursor.execute("INSERT INTO Versioning (version_name) VALUES ('Draft Version 0.2')")

# Commit changes and close connection
conn.commit()
conn.close()
