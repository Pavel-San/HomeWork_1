my_f = open('test.txt', 'w')
txt = input('Введите текст \n')
while txt:
    my_f.writelines(txt)
    txt = input('Введите текст \n')
    if not txt:
        break

my_f.close()

