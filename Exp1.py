# Write a program to print datatype of a variable

user_input = input("Enter a variable: ")

# Try to convert to integer
try:
    x = int(user_input)
except ValueError:
    # Try to convert to float
    try:
        x = float(user_input)
    except ValueError:
        # If both conversions fail, treat as string
        x = user_input

print(type(x))