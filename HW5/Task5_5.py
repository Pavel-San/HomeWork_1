def summary():
    try:
        with open('test_5.txt', 'w+') as file_obj:
            line = input('Введите числа через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неверно введено число')


summary()
