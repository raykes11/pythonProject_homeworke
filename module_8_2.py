def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result = result + number
        except:
            print(f'Некорректный тип данных для подсчёта суммы -{number}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    if isinstance(numbers, int) or isinstance(numbers, float):
        averg = None
        print(f'В numbers записан некорректный тип данных.')
        return averg
    else:
        list_ = personal_sum(numbers)
    try:
        etc = len(numbers)
        etc = etc - list_[1]
        averg = list_[0] / etc
    except ZeroDivisionError:
        return 0
    except TypeError:
        f'В {numbers} записан некорректный тип данных.'
    return averg


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
