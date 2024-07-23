first_number = int(input('Какое число выпало: '))
list = []

for pair_first in range(1, first_number):
    for pair_second in range(1, first_number):
        summa = pair_first + pair_second
        if pair_first == pair_second:
            continue
        elif first_number % summa == 0:
            list.append([pair_first,pair_second])

for cell in list:
    for cell_revers in list:
        if cell[0] == cell_revers[1] and cell[1] == cell_revers[0]:
            list.remove(cell_revers)

print(f'Введи следующие пары: {list}')