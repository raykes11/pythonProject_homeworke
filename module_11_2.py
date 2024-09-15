from requests import TooManyRedirects
class Object_:
    def __init__(self, name, age, *time):
        self.name = name
        self.age = age
        self.time = time
        self.etc = 0
        self.__drhdpfjf = 35

    def Oooops(self):
        pass


def Azaza(aaaaaaaaaaaaaa):
    a = aaaaaaaaaaaaaa
    return [a, a]


def introspection_info(obj):
    dict_ = {}
    dict_['type']  = obj.__class__.__name__
    dict_['attributes'] = [attributes for attributes in dir(obj) if callable(attributes)]
    dict_['methods'] = [methods for methods in dir(obj) if not callable(methods)]
    dict_['module'] = obj.__class__.__module__
    return dict_


number_info = introspection_info(42)
print(number_info)

