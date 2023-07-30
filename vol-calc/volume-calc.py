import math

# define the conversion constants
CUBIC_FOOT_TO_LITERS = 28.3168466
CUBIC_FOOT_TO_US_GALLONS = 7.48052
CUBIC_FOOT_TO_IMPERIAL_GALLONS = 6.22884

# The volume calculation functions
def calculate_rectangle_volume(length, width, height, unit):
    if unit == "mm":
        # convert mm to ft
        length = length / 304.8
        width = width / 304.8
        height = height / 304.8
    elif unit == "cm":
        # convert cm to ft
        length = length / 30.48
        width = width / 30.48
        height = height / 30.48
    elif unit == "in":
        # convert in to ft
        length = length / 12
        width = width / 12
        height = height / 12
    # calculate volume in cubic feet
    volume_ft3 = length * width * height
    # convert volume to liters and gallons
    volume_liters = volume_ft3 * CUBIC_FOOT_TO_LITERS
    volume_us_gallons = volume_ft3 * CUBIC_FOOT_TO_US_GALLONS
    volume_imperial_gallons = volume_ft3 * CUBIC_FOOT_TO_IMPERIAL_GALLONS
    return volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons

def calculate_hexagon_volume(side, height, unit):
    if unit == "mm":
        # convert mm to ft
        side = side / 304.8
        height = height / 304.8
    elif unit == "cm":
        # convert cm to ft
        side = side / 30.48
        height = height / 30.48
    elif unit == "in":
        # convert in to ft
        side = side / 12
        height = height / 12
    # calculate volume in cubic feet
    volume_ft3 = (3 * math.sqrt(3) / 2 * side ** 2) * height
    # convert volume to liters and gallons
    volume_liters = volume_ft3 * CUBIC_FOOT_TO_LITERS
    volume_us_gallons = volume_ft3 * CUBIC_FOOT_TO_US_GALLONS
    volume_imperial_gallons = volume_ft3 * CUBIC_FOOT_TO_IMPERIAL_GALLONS
    return volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons

def calculate_octagon_volume(side, height, unit):
    if unit == "mm":
        # convert mm to ft
        side = side / 304.8
        height = height / 304.8
    elif unit == "cm":
        # convert cm to ft
        side = side / 30.48
        height = height / 30.48
    elif unit == "in":
        # convert in to ft
        side = side / 12
        height = height / 12
    # calculate volume in cubic feet
    volume_ft3 = 2 * (1 + math.sqrt(2)) * side ** 2 * height
    # convert volume to liters and gallons
    volume_liters = volume_ft3 * CUBIC_FOOT_TO_LITERS
    volume_us_gallons = volume_ft3 * CUBIC_FOOT_TO_US_GALLONS
    volume_imperial_gallons = volume_ft3 * CUBIC_FOOT_TO_IMPERIAL_GALLONS
    return volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons

def calculate_flat_back_hex_bow_front_volume(side, height, radius, unit):
    if unit == "mm":
        # convert mm to ft
        side = side / 304.8
        height = height / 304.8
        radius = radius / 304.8
    elif unit == "cm":
        # convert cm to ft
        side = side / 30.48
        height = height / 30.48
        radius = radius / 30.48
    elif unit == "in":
        # convert in to ft
        side = side / 12
        height = height / 12
        radius = radius / 12
    # calculate volume of hexagonal part in cubic feet
    volume_hex_ft3 = 3 * math.sqrt(3) / 2 * side ** 2 * height
    # calculate volume of cylindrical part in cubic feet
    volume_cylinder_ft3 = math.pi * radius ** 2 * height
    # total volume in cubic feet
    volume_ft3 = volume_hex_ft3 + volume_cylinder_ft3
    # convert volume to liters and gallons
    volume_liters = volume_ft3 * CUBIC_FOOT_TO_LITERS
    volume_us_gallons = volume_ft3 * CUBIC_FOOT_TO_US_GALLONS
    volume_imperial_gallons = volume_ft3 * CUBIC_FOOT_TO_IMPERIAL_GALLONS
    return volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons

def calculate_cylinder_volume(radius, height, unit):
    if unit == "mm":
        # convert mm to ft
        radius = radius / 304.8
        height = height / 304.8
    elif unit == "cm":
        # convert cm to ft
        radius = radius / 30.48
        height = height / 30.48
    elif unit == "in":
        # convert in to ft
        radius = radius / 12
        height = height / 12
    # calculate volume in cubic feet
    volume_ft3 = math.pi * radius ** 2 * height
    # convert volume to liters and gallons
    volume_liters = volume_ft3 * CUBIC_FOOT_TO_LITERS
    volume_us_gallons = volume_ft3 * CUBIC_FOOT_TO_US_GALLONS
    volume_imperial_gallons = volume_ft3 * CUBIC_FOOT_TO_IMPERIAL_GALLONS
    return volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons

def calculate_half_cylinder_volume(radius, height, unit):
    # calculate the volume of the full cylinder
    volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons = calculate_cylinder_volume(radius, height, unit)
    # take half of the volumes
    volume_ft3 *= 0.5
    volume_liters *= 0.5
    volume_us_gallons *= 0.5
    volume_imperial_gallons *= 0.5
    return volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons

def calculate_quarter_cylinder_volume(radius, height, unit):
    # calculate the volume of the full cylinder
    volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons = calculate_cylinder_volume(radius, height, unit)
    # take a quarter of the volumes
    volume_ft3 *= 0.25
    volume_liters *= 0.25
    volume_us_gallons *= 0.25
    volume_imperial_gallons *= 0.25
    return volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons

def calculate_elliptical_volume(semi_major_axis, semi_minor_axis, unit):
    if unit == "mm":
        # convert mm to ft
        semi_major_axis = semi_major_axis / 304.8
        semi_minor_axis = semi_minor_axis / 304.8
    elif unit == "cm":
        # convert cm to ft
        semi_major_axis = semi_major_axis / 30.48
        semi_minor_axis = semi_minor_axis / 30.48
    elif unit == "in":
        # convert in to ft
        semi_major_axis = semi_major_axis / 12
        semi_minor_axis = semi_minor_axis / 12
    # calculate volume in cubic feet
    volume_ft3 = 4/3 * math.pi * semi_major_axis * semi_minor_axis ** 2
    # convert volume to liters and gallons
    volume_liters = volume_ft3 * CUBIC_FOOT_TO_LITERS
    volume_us_gallons = volume_ft3 * CUBIC_FOOT_TO_US_GALLONS
    volume_imperial_gallons = volume_ft3 * CUBIC_FOOT_TO_IMPERIAL_GALLONS
    return volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons

def calculate_corner_pentagon_volume(base_width, front_width, height, unit):
    if unit == "mm":
        # convert mm to ft
        base_width = base_width / 304.8
        front_width = front_width / 304.8
        height = height / 304.8
    elif unit == "cm":
        # convert cm to ft
        base_width = base_width / 30.48
        front_width = front_width / 30.48
        height = height / 30.48
    elif unit == "in":
        # convert in to ft
        base_width = base_width / 12
        front_width = front_width / 12
        height = height / 12
    # calculate volume in cubic feet
    volume_ft3 = 0.5 * (base_width + front_width) * height
    # convert volume to liters and gallons
    volume_liters = volume_ft3 * CUBIC_FOOT_TO_LITERS
    volume_us_gallons = volume_ft3 * CUBIC_FOOT_TO_US_GALLONS
    volume_imperial_gallons = volume_ft3 * CUBIC_FOOT_TO_IMPERIAL_GALLONS
    return volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons

def calculate_corner_prism_volume(base, height, depth, unit):
    if unit == "mm":
        # convert mm to ft
        base = base / 304.8
        height = height / 304.8
        depth = depth / 304.8
    elif unit == "cm":
        # convert cm to ft
        base = base / 30.48
        height = height / 30.48
        depth = depth / 30.48
    elif unit == "in":
        # convert in to ft
        base = base / 12
        height = height / 12
        depth = depth / 12
    # calculate volume in cubic feet
    volume_ft3 = 0.5 * base * height * depth
    # convert volume to liters and gallons
    volume_liters = volume_ft3 * CUBIC_FOOT_TO_LITERS
    volume_us_gallons = volume_ft3 * CUBIC_FOOT_TO_US_GALLONS
    volume_imperial_gallons = volume_ft3 * CUBIC_FOOT_TO_IMPERIAL_GALLONS
    return volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons

def calculate_bow_front_volume(length, width, height, radius, unit):
    if unit == "mm":
        # convert mm to ft
        length = length / 304.8
        width = width / 304.8
        height = height / 304.8
        radius = radius / 304.8
    elif unit == "cm":
        # convert cm to ft
        length = length / 30.48
        width = width / 30.48
        height = height / 30.48
        radius = radius / 30.48
    elif unit == "in":
        # convert in to ft
        length = length / 12
        width = width / 12
        height = height / 12
        radius = radius / 12
    # calculate volume of the rectangular part in cubic feet
    volume_rectangular_ft3 = length * width * height
    # calculate volume of the cylindrical part in cubic feet
    volume_cylindrical_ft3 = math.pi * radius ** 2 * length
    # total volume in cubic feet
    volume_ft3 = volume_rectangular_ft3 + volume_cylindrical_ft3
    # convert volume to liters and gallons
    volume_liters = volume_ft3 * CUBIC_FOOT_TO_LITERS
    volume_us_gallons = volume_ft3 * CUBIC_FOOT_TO_US_GALLONS
    volume_imperial_gallons = volume_ft3 * CUBIC_FOOT_TO_IMPERIAL_GALLONS
    return volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons

def calculate_aquarium_volume(shape, unit, measurements, output_unit_system):
    if shape.lower() == "rectangle" or shape.lower() == "cube" or shape.lower() == "l-shaped":
        volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons = calculate_rectangle_volume(*measurements, unit)
    elif shape.lower() == "hexagon":
        volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons = calculate_hexagon_volume(*measurements, unit)
    elif shape.lower() == "octagon":
        volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons = calculate_octagon_volume(*measurements, unit)
    elif shape.lower() == "flat back hexagon bow front":
        volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons = calculate_flat_back_hex_bow_front_volume(*measurements, unit)
    elif shape.lower() == "cylinder":
        volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons = calculate_cylinder_volume(*measurements, unit)
    elif shape.lower() == "half cylinder":
        volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons = calculate_half_cylinder_volume(*measurements, unit)
    elif shape.lower() == "quarter cylinder":
        volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons = calculate_quarter_cylinder_volume(*measurements, unit)
    elif shape.lower() == "elliptical":
        volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons = calculate_elliptical_volume(*measurements, unit)
    elif shape.lower() == "corner pentagon":
        volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons = calculate_corner_pentagon_volume(*measurements, unit)
    elif shape.lower() == "corner prism":
        volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons = calculate_corner_prism_volume(*measurements, unit)
    elif shape.lower() == "bow front":
        volume_ft3, volume_liters, volume_us_gallons, volume_imperial_gallons = calculate_bow_front_volume(*measurements, unit)
    else:
        return "Invalid shape"

    # truncate to 1 decimal point
    volume_liters = round(volume_liters, 1)
    volume_us_gallons = round(volume_us_gallons, 1)
    volume_imperial_gallons = round(volume_imperial_gallons, 1)

    # return the appropriate output based on the user's choice of unit system
    if output_unit_system.lower() == "metric":
        return str(volume_liters) + " liters"
    elif output_unit_system.lower() == "us":
        return str(volume_us_gallons) + " US gallons"
    elif output_unit_system.lower() == "uk":
        return str(volume_imperial_gallons) + " UK gallons"
    else:
        return "Invalid unit system"

def aquarium_volume_calculator():
    # display the available shapes
    print("Available shapes: rectangle, cube, l-shaped, hexagon, octagon, flat back hexagon bow front, cylinder, half cylinder, quarter cylinder, elliptical, corner pentagon, corner prism")
    
    # ask for the shape of the aquarium
    shape = input("Enter the shape of the aquarium: ").lower()
    
    # ask for the unit of the measurements
    unit = input("Enter the unit of the measurements (mm, cm, in, ft): ").lower()
    
    # ask for the measurements based on the shape
    if shape in ["rectangle", "cube", "l-shaped"]:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
        measurements = [length, width, height]
    elif shape in ["hexagon", "octagon"]:
        side = float(input("Enter the side length: "))
        height = float(input("Enter the height: "))
        measurements = [side, height]
    elif shape == "flat back hexagon bow front":
        side = float(input("Enter the side length: "))
        height = float(input("Enter the height: "))
        radius = float(input("Enter the radius: "))
        measurements = [side, height, radius]
    elif shape in ["cylinder", "half cylinder", "quarter cylinder"]:
        radius = float(input("Enter the radius: "))
        height = float(input("Enter the height: "))
        measurements = [radius, height]
    elif shape == "elliptical":
        semi_major_axis = float(input("Enter the semi-major axis length: "))
        semi_minor_axis = float(input("Enter the semi-minor axis length: "))
        measurements = [semi_major_axis, semi_minor_axis]
    elif shape == "corner pentagon":
        base_width = float(input("Enter the base width: "))
        front_width = float(input("Enter the front width: "))
        height = float(input("Enter the height: "))
        measurements = [base_width, front_width, height]
    elif shape == "corner prism":
        base = float(input("Enter the base length: "))
        height = float(input("Enter the height: "))
        depth = float(input("Enter the depth: "))
        measurements = [base, height, depth]
    elif shape == "bow front":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
        radius = float(input("Enter the radius of the bow front: "))
        measurements = [length, width, height, radius]
    else:
        print("Invalid shape")
        return

    # ask for the output unit system
    output_unit_system = input("Enter the output unit system (metric, US, UK): ").lower()

    # calculate the volume and print the result
    volume = calculate_aquarium_volume(shape, unit, measurements, output_unit_system)
    print("The volume of the aquarium is:", volume)

# Call the function to start the program
aquarium_volume_calculator()
