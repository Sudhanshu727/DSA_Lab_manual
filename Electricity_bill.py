def calculate_electricity_bill(units):
    """
    Calculate electricity bill based on units consumed.
    Rates:
        - First 100 units: ₹5 per unit
        - Next 100 units (101-200): ₹7 per unit
        - Above 200 units: ₹10 per unit
    """
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    
    return bill

def calculate_units(power_watts, hours):
    """
    Calculate units (kWh) from power rating in watts and hours used.
    """
    return (power_watts * hours) / 1000

def main():
    # Dictionary to store devices and their fixed power ratings
    devices = {
        "LED Lights (10)": {"power": 10 * 12, "hours": 0},  # 10 LEDs at 12W each
        "Fans (5)": {"power": 5 * 100, "hours": 0},         # 5 Fans at 100W each
        "AC": {"power": 1500, "hours": 0},                  # 1 AC at 1500W
        "Fridge": {"power": 300, "hours": 0},               # 1 Fridge at 300W
        "Heater": {"power": 2400, "hours": 0},              # 1 Heater at 2400W
        "Miscellaneous": {"power": 0, "hours": 0}           # Power to be entered by user
    }
    
    print("Fixed power ratings:")
    print("- 10 LED lights: 12W each (Total: 120W)")
    print("- 5 Fans: 100W each (Total: 500W)")
    print("- 1 AC: 1500W")
    print("- 1 Fridge: 300W")
    print("- 1 Heater: 2400W")
    print()
    
    # Get input for hours of usage for devices with fixed power
    for device_name in ["LED Lights (10)", "Fans (5)", "AC", "Fridge", "Heater"]:
        try:
            devices[device_name]["hours"] = float(input(f"Enter hours of usage for {device_name} per day: "))
        except ValueError:
            print(f"Invalid input for {device_name}. Setting hours to 0.")
            devices[device_name]["hours"] = 0
    
    # Get both power and hours for Miscellaneous
    try:
        devices["Miscellaneous"]["power"] = float(input(f"Enter power rating for Miscellaneous (watts): "))
        devices["Miscellaneous"]["hours"] = float(input(f"Enter hours of usage for Miscellaneous per day: "))
    except ValueError:
        print(f"Invalid input for Miscellaneous. Setting values to 0.")
        devices["Miscellaneous"]["power"] = 0
        devices["Miscellaneous"]["hours"] = 0
    
    # Ask for number of days
    try:
        num_days = int(input("\nEnter number of days for bill calculation: "))
        if num_days <= 0:
            print("Invalid number of days. Using 30 days as default.")
            num_days = 30
    except ValueError:
        print("Invalid input for number of days. Using 30 days as default.")
        num_days = 30
    
    # Calculate total units
    total_units = 0
    print("\nDevice Usage Summary:")
    print("-" * 60)
    print(f"{'Device':<20} {'Power (W)':<10} {'Hours':<10} {'Units (kWh)':<15}")
    print("-" * 60)
    
    for device_name, details in devices.items():
        device_units = calculate_units(details["power"], details["hours"])
        total_units += device_units
        print(f"{device_name:<20} {details['power']:<10.2f} {details['hours']:<10.2f} {device_units:<15.2f}")
    
    print("-" * 60)
    print(f"Total Units Consumed per day: {total_units:.2f} kWh")
    
    # Calculate bill for specified number of days
    period_units = total_units * num_days
    bill = calculate_electricity_bill(period_units)
    print(f"\nEstimated Consumption for {num_days} days: {period_units:.2f} units")
    print(f"Estimated Electricity Bill for {num_days} days: ₹{bill:.2f}")

if __name__ == "__main__":
    main()