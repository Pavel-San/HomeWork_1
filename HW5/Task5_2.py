my_f = open('test_2.txt', 'r')
content = my_f.read()
my_f = open('test_2.txt', 'r')
content = my_f.readlines()
print(f'Количество строк в файле - {len(content)}')
my_f = open('test_2.txt', 'r')
content = my_f.readlines()
for i in range(len(content)):
    print(f'Количество символов в {i + 1} строке {len(content[i])}')
my_f = open('test_2.txt', 'r')
content = my_f.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_f.close()
