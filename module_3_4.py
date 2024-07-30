def single_root_words (root_word, *other_words):
    root_word = str(root_word).upper().lower()
    list_ = []
    for word in other_words:
        word_custom = str(word).upper().lower()
        if word_custom.find(root_word) >= 0:
            list_.append(word)
            continue
        elif root_word.find(word_custom) >= 0:
            list_.append(word)
            continue
    return list_

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

