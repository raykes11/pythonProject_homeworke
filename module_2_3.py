my_list =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
cell_number = 0

while len(my_list) >= cell_number + 1:
    if my_list[ cell_number ] == 0:
        cell_number = cell_number + 1
        continue
    elif my_list[ cell_number ] > 0:
        print(my_list[ cell_number ])
        cell_number = cell_number + 1
    else:
        cell_number = cell_number + 1
        break