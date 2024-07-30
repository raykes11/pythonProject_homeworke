#Вариант 1, с двумя зависимыми функциями

def search_string (*any):
    string_list = []
    for type_ in any:
        if isinstance(type_, str):
            string_list.append(type_)
        if isinstance(type_, list) or isinstance(type_, tuple) or isinstance(type_,set):
            for component in type_:
                for element in search_string(component):
                    string_list.append(element)
        elif isinstance(type_,dict):
            for key in type_:
                if isinstance(key,str):
                    string_list.append(key)
                if isinstance(type_[key], list) or isinstance(type_[key], tuple) or isinstance(type_[key],dict) or isinstance(type_[key],set):
                    for element in search_string(type_[key]):
                        string_list.append(element)
                elif isinstance(type_[key], str):
                     string_list.append(type_[key])
                else:
                    continue
        else:
            continue
    return string_list

def search_int_float_bool (*any):
    numbers_list = []
    for type_ in any:
        if isinstance(type_, bool):
            numbers_list.append(int(type_))
        elif isinstance(type_,int) or isinstance(type_, float):
            numbers_list.append(type_)
        elif isinstance(type_, list) or isinstance(type_, tuple) or isinstance(type_,set):
            for component in type_:
                for element in search_int_float_bool(component):
                    numbers_list.append(element)
        elif isinstance(type_,dict):
            for key in type_:
                if isinstance(key,int) or isinstance(key,float):
                    numbers_list.append(key)
                if isinstance(type_[key], list) or isinstance(type_[key], tuple) or isinstance(type_[key],dict) or isinstance(type_[key],set):
                    for element in search_int_float_bool(type_[key]):
                        numbers_list.append(element)
                elif isinstance(type_[key], bool):
                    numbers_list.append(int(type_[key]))
                elif isinstance(type_[key], int) or isinstance(type_, float):
                    numbers_list.append(type_[key])
                else:
                    continue
        else:
            continue
    return numbers_list

def summ_all_element (*any):
    number_list = []
    summ = 0
    for string in search_string(any):
        str_number = int(len(string))
        number_list.append(str_number)
    for element in search_int_float_bool(any):
        number_list.append(element)
    for number in number_list:
        summ = summ + number
    return summ



#Вариант 2, одной функцией
def summ_all_element_2 (*any):
    numbers_list = []
    summ = 0
    for type_ in any:
        if isinstance(type_, str):
            numbers_list.append(len(type_))
        elif isinstance(type_, bool):
            numbers_list.append(int(type_))
        elif isinstance(type_,int) or isinstance(type_, float):
            numbers_list.append(type_)
        elif isinstance(type_, list) or isinstance(type_, tuple) or isinstance(type_,set):
            for component in type_:
                    summ = summ + summ_all_element_2(component)
        elif isinstance(type_,dict):
            for key in type_:
                if isinstance(key,str):
                    numbers_list.append(len(key))
                elif isinstance(key,int) or isinstance(key,float):
                    numbers_list.append(key)
                if isinstance(type_[key], list) or isinstance(type_[key], tuple) or isinstance(type_[key],dict) or isinstance(type_[key],set):
                    summ= summ + summ_all_element_2(type_[key])
                elif isinstance(type_[key], bool):
                    numbers_list.append(int(type_[key]))
                elif isinstance(type_[key], int) or isinstance(type_, float):
                    numbers_list.append(type_[key])
                else:
                    continue
        else:
            continue
    for number in numbers_list:
        summ = summ + number
    return summ



data_structure = [[1, 2, 3],  {'a': 4, 'b': 5},  (6, {'cube': 7, 'drum': 8}),  "Hello",  ((), [{(2, 'Urban', ('Urban2', 35))}]) ]




print(summ_all_element_2(data_structure))
#
# print(search_string (data_structure))
# print(search_int_float_bool(data_structure))
print(summ_all_element(data_structure))
# print(search_int_and_float(True,False))