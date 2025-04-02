def tower_of_hanoi(n, source, auxiliary, destination):
    """
    Solve Tower of Hanoi puzzle using recursion
    Parameters:
        n (int): Number of disks
        source (str): Source rod name
        auxiliary (str): Helper rod name
        destination (str): Destination rod name
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Move n-1 disks from source to auxiliary using destination as helper
    tower_of_hanoi(n-1, source, destination, auxiliary)
    
    # Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Move n-1 disks from auxiliary to destination using source as helper
    tower_of_hanoi(n-1, auxiliary, source, destination)

# Get number of disks from user
n = int(input("Enter number of disks: "))
if n <= 0:
    print("Please enter a positive number!")
else:
    print("\nSteps to solve Tower of Hanoi:")
    tower_of_hanoi(n, 'A', 'B', 'C')
    print(f"\nTotal number of moves: {2**n - 1}")