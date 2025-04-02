def generate_pascal_triangle(rows):
    """
    Generate Pascal's Triangle for given number of rows
    Parameters:
        rows (int): Number of rows to generate
    Returns:
        list: 2D list containing Pascal's Triangle values
    """
    triangle = []
    
    for i in range(rows):
        # Create a new row
        current_row = []
        
        for j in range(i + 1):
            # First and last elements are always 1
            if j == 0 or j == i:
                current_row.append(1)
            else:
                # Add the two numbers from the row above
                above_row = triangle[i-1]
                current_row.append(above_row[j-1] + above_row[j])
                
        triangle.append(current_row)
    
    return triangle

def print_pascal_triangle(triangle):
    """
    Print Pascal's Triangle in a formatted way
    Parameters:
        triangle (list): 2D list containing Pascal's Triangle values
    """
    rows = len(triangle)
    # Calculate width needed for formatting
    width = len(' '.join(map(str, triangle[-1])))
    
    for row in triangle:
        # Convert numbers to strings and center the row
        numbers = ' '.join(map(str, row))
        print(numbers.center(width))

def main():
    try:
        # Get number of rows from user
        rows = int(input("Enter number of rows for Pascal's Triangle: "))
        if rows <= 0:
            print("Please enter a positive number!")
            return
            
        # Generate and print the triangle
        triangle = generate_pascal_triangle(rows)
        print("\nPascal's Triangle:")
        print_pascal_triangle(triangle)
        
    except ValueError:
        print("Please enter a valid integer!")

if __name__ == "__main__":
    main()