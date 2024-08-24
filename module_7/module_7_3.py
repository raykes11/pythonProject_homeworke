class WordsFinder:
    file_names = []

    def __init__(self, *args):
        for name in args:
            self.file_names.append(name)

    def get_all_words(self):
        all_words = {}
        del_symboll = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for len_ in range(len(self.file_names)):
            with open(self.file_names[len_], 'r', encoding='utf-8') as file:
                word = file.read().lower()
                for symbol in del_symboll:
                    word = word.replace(symbol, '')
                word = word.split()
                all_words[self.file_names[len_]] = word
        return all_words

    def count(self, name_book, count):
        dict_ = self.get_all_words()
        stroka = dict_[name_book].count(count.lower())
        return {name_book: stroka}

    def find(self, name_book, find):
        dict_ = self.get_all_words()
        stroka = dict_[name_book]
        number_cell = 0
        for word in stroka:
            number_cell += 1
            if word == find.lower():
                break
        return {name_book: number_cell}


finder1 = WordsFinder('test_file.txt', 'Walt Whitman - O Captain! My Captain!.txt', 'Rudyard Kipling - If.txt')

print(finder1.find('Walt Whitman - O Captain! My Captain!.txt', 'captain'))
print(finder1.count('Walt Whitman - O Captain! My Captain!.txt', 'captain'))
print(finder1.find('Rudyard Kipling - If.txt', 'if'))
print(finder1.count('Rudyard Kipling - If.txt', 'if'))
print(finder1.get_all_words())
