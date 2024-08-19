class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self,owner,__model,__color,__engine_power):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__color = str(__color)
        self.__engine_power = int(__engine_power)
    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя:  {self.__engine_power}"

    def get_color(self):
        return f"Цвет:  {self.__color}"

    def print_info(self):
        return print(f'''
        {self.get_model()}
        {self.get_horsepower()}
        {self.get_color()}
        Владелец: {self.owner}.''')

    def set_color(self,new_color):
        if new_color.upper().lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.upper().lower()
            return self
        else:
            print(f'Нельзя изменить цвет на {new_color.upper().lower()}')



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
