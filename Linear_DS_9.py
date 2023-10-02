def reverse_stack(stack): 
    """Reverse a stack. Args: stack: A list representing a stack. Returns: None. The stack is reversed in place. 
    """ 
    reversed_stack = [] 
    while stack: 
        reversed_stack.append(stack.pop()) 
    while reversed_stack: 
        stack.append(reversed_stack.pop()) 
# Example usage: 
stack = [1, 2, 3, 4, 5] 
reverse_stack(stack) 
print(stack)
