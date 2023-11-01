def find_common_elements(list1, list2):
    
    # This function takes two lists as input and returns a new list containing the common elements between the two input lists.
    
    common_elements = []
    for element in list1:
        if element in list2 and element not in common_elements:
            common_elements.append(element)
    return common_elements

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(list1, list2)
print(common_elements)
