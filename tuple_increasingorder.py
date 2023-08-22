def sort_tuples_by_last_element(input_list): 
    return sorted(input_list, key=lambda x: x[-1]) 
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
sorted_list = sort_tuples_by_last_element(sample_list) 
print(sorted_list)