def test_function(a):
    test = type(a)
    def inner_function(test):
        print("Я в области видимости функции test_function")
    inner_function(a)
    return test

print(test_function(4))
# inner_function(3)