def find_pairs(array, sum): 
    """Find all pairs of an integer array whose sum is equal to a given number. 
    Args: 
    array: A list of integers. 
    sum: The sum to match. 
    Returns: A list of tuples, where each tuple contains a pair of integers from the array that sum to the given number. 
    """ 
    pairs = [] 
    for i in range(len(array)): 
        for j in range(i + 1, len(array)): 
            if array[i] + array[j] == sum: 
                pairs.append((array[i], array[j])) 
                return pairs 
# Example usage: 
array = [1, 2, 3, 4, 5] 
sum = 5 
pairs = find_pairs(array, sum) 
print(pairs)
