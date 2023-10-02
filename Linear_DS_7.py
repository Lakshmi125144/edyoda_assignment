def prefix_to_infix(prefix_expression): 
    """Convert a prefix expression to an infix expression. Args: prefix_expression: A string representing a prefix expression. Returns: A string representing the equivalent infix expression. 
    """ 
    stack = [] 
    for token in prefix_expression.split()[::-1]: 
        if token not in ["+", "-", "*", "/"]: 
            stack.append(token) 
        else: 
            operand1 = stack.pop() 
            operand2 = stack.pop() 
            operator = token 
            expression = f"({operand1} {operator} {operand2})" 
            stack.append(expression) 
    return stack.pop() 
# Example usage: 
prefix_expression = "-+AB*CD" 
infix_expression = prefix_to_infix(prefix_expression) 
print(infix_expression)