def calculate_battery_power(mah, voltage):
    """
    Calculate battery power in watt-hours (Wh)
    Parameters:
        mah (float): Battery capacity in milliampere-hours
        voltage (float): Battery voltage in volts
    Returns:
        float: Battery power in watt-hours
    """
    # Convert mAh to Ah by dividing by 1000
    amp_hours = mah / 1000
    # Calculate watt-hours (Power = Voltage * Current)
    watt_hours = voltage * amp_hours
    return watt_hours

def main():
    try:
        # Get input from user
        battery_mah = float(input("Enter battery capacity (mAh): "))
        battery_voltage = float(input("Enter battery voltage (V): "))
        
        # Calculate power
        power = calculate_battery_power(battery_mah, battery_voltage)
        
        # Display results
        print(f"\nBattery Specifications:")
        print(f"Capacity: {battery_mah} mAh")
        print(f"Voltage: {battery_voltage} V")
        print(f"Power: {power:.2f} Wh")
        
    except ValueError:
        print("Please enter valid numeric values!")

if __name__ == "__main__":
    main()