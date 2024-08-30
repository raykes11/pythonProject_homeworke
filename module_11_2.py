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
    print(dict_['attributes'])
    print(dict_)


a = {"we": 34, 'ewgfe': 35466778}

# introspection_info((45,0))
introspection_info(Azaza)
introspection_info(Object_(254045, 2, 2, 2, ))
