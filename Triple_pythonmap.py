# Sample list of integers
numbers = [11, 2, 3, 4, 5, 6, 7] 
# Define a lambda function to triple a number 
triple = lambda x: x * 3 
# Use map to apply the lambda function to each element in the list 
result = list(map(triple, numbers)) 
# Print the tripled numbers 
print("Triple of list numbers:") 
print(result)