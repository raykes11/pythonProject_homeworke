def is_prime(func):
    def prime(*args):
        number = func(*args)
        flag = True
        for i in range(2, number):
            if number % i == 0:
                flag = False
                break
        if flag:
            print('Простое')
        else:
            print('Составное')
        return number

    return prime


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(1, 1, 2004981)
print(result)
