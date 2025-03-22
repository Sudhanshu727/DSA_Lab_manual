def get_resistor_value(band1, band2, multiplier, tolerance="no_color"):
    color_codes = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9
    }
    
    multiplier_codes = {
        "black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10000,
        "green": 100000, "blue": 1000000, "violet": 10000000, "gray": 100000000, "white": 1000000000
    }
    
    tolerance_codes = {
        "gold": 5, "silver": 10 ,"no_color": 20
    }
    
    if band1 not in color_codes or band2 not in color_codes or multiplier not in multiplier_codes:
        return "Invalid color input!"
    
    resistance_value = (color_codes[band1] * 10 + color_codes[band2]) * multiplier_codes[multiplier]
    
    if tolerance:
        if tolerance in tolerance_codes:
            return f"Resistance: {resistance_value} Ω ± {tolerance_codes[tolerance]}%"
        else:
            return "Invalid tolerance color!"
    
    return f"Resistance: {resistance_value} Ω"

band1 = input("Enter the first band color: ").strip().lower()
band2 = input("Enter the second band color: ").strip().lower()
multiplier = input("Enter the multiplier band color: ").strip().lower()
tolerance = input("Enter the tolerance band color (optional, press Enter to skip): ").strip().lower()

if not tolerance:
    print(get_resistor_value(band1, band2, multiplier))
else:
    print(get_resistor_value(band1, band2, multiplier, tolerance))
