a = float(input('Введите делимое:'))
b = float(input('Введите делитель:'))


def func_1(a, b):
    return a / b


try:
    a / b
except ZeroDivisionError:
    print('На ноль делить нельзя')
else:
    print(func_1(a, b))
