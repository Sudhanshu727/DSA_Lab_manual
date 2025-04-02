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

# Get the number of units consumed from the user
try:
    units = int(input("Enter the number of units consumed: "))
    if units < 0:
        print("Units cannot be negative. Please enter a valid number.")
    else:
        bill = calculate_electricity_bill(units)
        print(f"Electricity Bill for {units} units: ₹{bill}")
except ValueError:
    print("Please enter a valid integer for the number of units.")