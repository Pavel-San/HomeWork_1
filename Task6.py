a = int(input('Введите результат в первый день, км:'))
b = int(input('Введите цель, км:'))
c = 0
while a <= b:
    a = round(a + a * 0.1, 2)
    c = c + 1
    print(c, '-й День:', a)
print('Ответ: на', c, 'день спортсмен достиг результата — не менее', b, 'км')