first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [len(x[0]) - len(x[1]) for x in zip(first, second) if len(x[0]) - len(x[1]) != 0]
second_result = [True if len(y) == len(x) else False for y in first for x in second for i in range(3) if
                 first[i] == y and second[i] == x]

print(first_result)
print(second_result)
