def postfix_to_prefix(postfix_expression): 
    """Convert a postfix expression to a prefix expression. Args: postfix_expression: A string representing a postfix expression. Returns: A string representing the equivalent prefix expression. 
    """ 
    stack = [] 
    for token in postfix_expression.split(): 
        if token not in ["+", "-", "*", "/"]: 
            stack.append(token) 
        else: 
            operand1 = stack.pop() 
            operand2 = stack.pop() 
            operator = token 
            expression = f"{operator} {operand2} {operand1}" 
            stack.append(expression) 
    return stack.pop() 
# Example usage: 
postfix_expression = "AB+CD-*" 
prefix_expression = postfix_to_prefix(postfix_expression) 
print(prefix_expression)