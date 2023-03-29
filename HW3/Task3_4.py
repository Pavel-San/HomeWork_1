x = int(input('Введите положительное целое число: '))
if x <= 0:
    print('Ошибка ввода')
else:
    y = int(input('Введите целое отрицательное число: '))
    if y >= 0:
        print('Ошибка ввода')
    else:
        def my_func(x, y):
            return (x ** y)


_____________________________________


def my_func(x, y):
    z = 1
    res = 1 / x
    while z < abs(y):
        res = res * (1 / x)
        z += 1
    return res



