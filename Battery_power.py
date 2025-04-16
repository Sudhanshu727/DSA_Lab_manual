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

def calculate_battery_capacity(current, hours):
    """
    Calculate battery capacity in milliampere-hours (mAh)
    Parameters:
        current (float): Current in amperes (A)
        hours (float): Time in hours (h)
    Returns:
        float: Battery capacity in milliampere-hours (mAh)
    """
    # Convert current from amperes to milliamperes and calculate capacity
    mah = current * 1000 * hours
    return mah

# Typical specifications for AA and AAA batteries
aa_capacity = 2000  # in mAh
aaa_capacity = 1000  # in mAh
voltage = 1.5  # in volts (same for both AA and AAA)

# Calculate power for AA and AAA batteries
aa_power = calculate_battery_power(aa_capacity, voltage)
aaa_power = calculate_battery_power(aaa_capacity, voltage)

# Compare and display the results
print("Battery Power Comparison:")
print(f"AA Battery: {aa_capacity} mAh, {voltage} V -> {aa_power:.2f} Wh")
print(f"AAA Battery: {aaa_capacity} mAh, {voltage} V -> {aaa_power:.2f} Wh")

if aa_power > aaa_power:
    print("\nAA battery has more power than AAA battery.")
elif aa_power < aaa_power:
    print("\nAAA battery has more power than AA battery.")
else:
    print("\nAA and AAA batteries have the same power.")

# Get input from the user
try:
    current = float(input("Enter the current (in amperes): "))
    hours = float(input("Enter the time (in hours): "))
    
    if current < 0 or hours < 0:
        print("Current and time must be non-negative values.")
    else:
        # Calculate battery capacity
        battery_capacity = calculate_battery_capacity(current, hours)
        print(f"\nBattery capacity: {battery_capacity:.2f} mAh")
except ValueError:
    print("Please enter valid numeric values for current and time.")