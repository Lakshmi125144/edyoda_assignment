def find_first_non_repeated_character(string): 
    """Find the first non-repeated character from a string. Args: string: A string. Returns: The first non-repeated character from the string, or None if there is no such character. 
    """ 
    character_frequencies = {} 
    for character in string: 
        if character not in character_frequencies: character_frequencies[character] = 0 
        character_frequencies[character] += 1 
    for character in string: 
        if character_frequencies[character] == 1: 
            return character 
    return None 
# Example usage: 
string = "abcabcbb" 
first_non_repeated_character = find_first_non_repeated_character(string) 
print(first_non_repeated_character)
