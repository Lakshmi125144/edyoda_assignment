def are_rotations(string1, string2): 
    """Check if two strings are a rotation of each other. Args: string1: A string. string2: A string. Returns: True if the strings are a rotation of each other, False otherwise. 
    """ 
    if len(string1) != len(string2): 
        return False combined_string = string1 + string1 
        return string2 in combined_string 
 # Example usage: 
string1 = "waterbottle" string2 = "tlewaterbo" are_rotations = are_rotations(string1, string2) 
print(are_rotations)
