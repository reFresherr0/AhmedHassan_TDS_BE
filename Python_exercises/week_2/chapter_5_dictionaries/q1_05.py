def combine_dictionaries(dict1, dict2):
    #combined_dict = {}
    #combined_dict.update(dict1)
    #combined_dict.update(dict2)
    #return combined_dict
    
    return {**dict1, **dict2}

# Test:
print(combine_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))