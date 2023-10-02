def find_smallest_number_using_stack(stack): 
    """Find the smallest number using a stack. Args: stack: A list representing a stack. Returns: The smallest number in the stack. 
    """ 
    smallest_number = stack[0] 
    while stack: 
        number = stack.pop() 
        if number < smallest_number: 
            smallest_number = number 
    return smallest_number 
# Example usage: 
stack = [1, 2, 3, 4, 5] 
smallest_number = find_smallest_number_using_stack(stack) 
print(smallest_number)