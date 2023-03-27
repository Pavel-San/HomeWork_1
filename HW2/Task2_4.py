my_list = input('Введите слова через пробел:').split(' ')
l = 1
for word in my_list:
    if len(word) > 10:
        print(f'{l}.{word[:10]}')
    else:
        print(f'{l}.{word}')
    l += 1
print()
