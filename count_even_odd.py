numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
even = 0 
odd = 0 
x = 0 
while x < len(numbers): 
    if numbers[x] % 2 == 0: 
        even += 1 
    else: 
        odd += 1 
    x += 1 
print("Number of even numbers:", even) 
print("Number of odd numbers:", odd)