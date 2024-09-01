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
    # print(obj.__name__)
    type_ = type(obj)
    dict_['type'] = str(type_)[8:-2]
    get_ = [getattr(obj, a) for a in dir(obj)]
    dict_['attributes'] = [list(a.keys()) for a in get_ if isinstance(a, dict) and len(a) > 0]
    dict_['methods'] = dir(obj)
    dict_['module'] = __name__
    return dict_


number_info = introspection_info(42)
print(number_info)
