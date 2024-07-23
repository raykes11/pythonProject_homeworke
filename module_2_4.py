numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for unit in numbers:
    if unit == 1:
        continue
    elif len(primes) == 0:
        primes.append(unit)
        continue
    is_prime = True # сколько раз удалось поделить без остатка
    for simpl_number in primes:
        if unit % simpl_number != 0:
            continue
        else:
            is_prime = False
            break
    if is_prime:
        primes.append(unit)
    else:
        not_primes.append(unit)

print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')
