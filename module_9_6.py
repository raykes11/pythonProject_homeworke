def all_variants(text):
    iter_ = 0
    while iter_ < len(text):
        for i in range(len(text) - iter_):
            text_ = list(text)
            yield f"{''.join(text_[i:i + iter_ + 1])}"
        iter_ += 1


a = all_variants('123456')

for i in a:
    print(i)
