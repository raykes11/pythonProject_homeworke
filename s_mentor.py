file = open('s_mentor.txt', 'r+', encoding='utf-8')
include = file.read()
# print(include)
include = include.replace('\n', ',').replace(' ', '')
include = list(include.split(','))
volium = []
all_ = []
b = True
c = True
for iter in include:
    if iter == '':
        pass
    elif b and c:
        volium.append(iter)
        b = False
    elif b == False and c == True:
        volium.append(iter)
        c = False
    elif b == False and c == False:
        volium.append(iter)
        b = True
        c = True
        all_.append(volium)
        print(all_)
        volium.clear()
print(all_)




all_ = []
b = ['Potato', '50.5', 'Vegetables']
c = ['Spaghetti', '3.4', 'Groceries']
d = ['Potato', '5.5', 'Vegetables']
g = [b, c, d]
for i in g:
    all_.append(i)

print(all_)
