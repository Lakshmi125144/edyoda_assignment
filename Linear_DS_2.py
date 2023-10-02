def reverse_array(array): 
    """Reverse an array in place. Args: array: A list of integers. Returns: None. The array is reversed in place. 
    """ 
    start = 0 
    end = len(array) - 1 
    while start < end: 
        array[start], array[end] = array[end], array[start] start += 1 end -= 1 
# Example usage: 
array = [1, 2, 3, 4, 5]  
reverse_array(array) 
print(array)
