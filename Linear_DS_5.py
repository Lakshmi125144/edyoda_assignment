def tower_of_hanoi(n, source, auxiliary, destination): 
    """Solve the Tower of Hanoi puzzle. Args: n: The number of disks. source: The source rod. auxiliary: The auxiliary rod. destination: The destination rod. 
    """ 
    if n == 1: 
        print(f"Move disk 1 from {source} to {destination}") 
    return tower_of_hanoi(n - 1, source, destination, auxiliary) 
print(f"Move disk {n} from {source} to {destination}") 
tower_of_hanoi(n - 1, auxiliary, source, destination) 
# Example usage: 
tower_of_hanoi(3, "A", "B", "C")