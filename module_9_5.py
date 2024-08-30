class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        else:
            self.step = step
        self.pointer = 0
        self.__iter = 1

    def __iter__(self):
        self.pointer = self.start
        self.__iter = 1
        return self

    def __next__(self):
        if self.__iter == 1 and self.valid_step():
            self.__iter += 1
        else:
            self.pointer = self.pointer + self.step
            if self.valid_step():
                pass
        return self.pointer

    def valid_step(self):
        if self.step < 0 and self.pointer < self.stop:
            raise StopIteration()
        elif self.step > 0 and self.pointer > self.stop:
            raise StopIteration()
        return True


class StepValueError(ValueError):
    def __init__(self, messenger):
        self.messenger = messenger


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)
print()

for i in iter2:
    print(i, end=' ')

print('\n')

for i in iter3:
    print(i, end=' ')

print('\n')

for i in iter4:
    print(i, end=' ')

print('\n')

for i in iter5:
    print(i, end=' ')

print('\n')
