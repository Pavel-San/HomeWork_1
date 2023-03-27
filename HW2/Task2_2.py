my_list = input('Введите числа через запятую:').split(',')
i = 0
n = 1
while len(my_list) > n:
    my_list[i], my_list[n] = my_list[n], my_list[i]
    i += 2
    n += 2
print('Список:', my_list)
