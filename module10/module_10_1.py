import time
from threading import Thread


def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for word in range(word_count):
            word += 1
            file.write(f'Какое-то слово № {word}\n')
            time.sleep(0.1)
    return print(f'Завершилась запись в файл {file_name}')


start = time.time()
first = wite_words(10, '../example1.txt')
second = wite_words(30, '../example2.txt')
third = wite_words(200, '../example3.txt')
fourth = wite_words(100, '../example4.txt')

print(time.time() - start)
start_ = time.time()

a = Thread(target=wite_words, args=(10, 'example5.txt'))
b = Thread(target=wite_words, args=(30, 'example6.txt'))
c = Thread(target=wite_words, args=(200, 'example7.txt'))
d = Thread(target=wite_words, args=(100, 'example8.txt'))

a.start()
b.start()
c.start()
d.start()

a.join()
b.join()
c.join()
d.join()

print(time.time() - start_)
