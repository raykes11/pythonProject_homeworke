first = int(input('В ведите провое число: '))
second = int(input('В ведите второе число: '))
third = int(input('В ведите третье число: '))

if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
