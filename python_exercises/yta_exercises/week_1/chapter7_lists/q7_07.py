list = [1, 2, 3, 4, 5]

reversed_list = []      # Empty list to store the reversed elements


for i in range(len(list)-1, -1, -1):    # iterate over the original list in reverse order
    reversed_list.append(list[i])

print('Original list:', list)
print('Reversed list:', reversed_list)
