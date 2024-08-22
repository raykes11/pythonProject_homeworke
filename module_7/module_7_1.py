class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r', encoding='utf-8')
        include = file.read()
        file.closed
        return include

    def add(self, *products):
        for product in products:
            file = open(self.__file_name, 'r+', encoding='utf-8')
            include = file.read()
            include_ = include.replace('\n', ',').replace(' ', '')
            include_ = list(include_.split(','))
            volium = []
            availability = []
            parametr = 0
            for iter in include_:
                if iter == '':
                    pass
                elif parametr == 0:
                    volium.append(iter)
                    parametr += 1
                elif parametr == 1:
                    volium.append(iter)
                    parametr += 1
                elif parametr == 2:
                    volium.append(iter)
                    availability.append(volium.copy())
                    parametr = 0
                    volium.clear()
            if len(include) == 0:
                file.write(f'{product.__str__()}\n')
            else:
                flag = True
                for position in range(len(availability)):
                    if product.name in availability[position][0] and str(product.weight) == str(
                            availability[position][1]):
                        print(f'Продукт {product} уже есть в магазине')
                        flag = False
                        break
                if flag:
                    file.write(f'{product.__str__()}\n')
            file.closed


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
