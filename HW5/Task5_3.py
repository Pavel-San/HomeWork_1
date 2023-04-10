my_file = open('sal.txt', 'r', encoding='utf-8')
sal = []
poor = []
my_list = my_file.read().split('\n')
for i in my_list:
    i = i.split()
    if int(i[1]) < 20000:
        poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 у сотрудников {poor},'
      f' средний оклад cотрудников менее 20000 составляет: {sum(map(int, sal)) / len(sal)}')
