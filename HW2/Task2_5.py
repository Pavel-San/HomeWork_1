rat = [7, 5, 3, 3, 2]
print(f"Текущий рейтинг: {rat}")
new_rat = int(input("Введите новый элемент рейтинга: "))
if new_rat > 0:
    rat.append(new_rat)
    rat.sort(reverse=True)
    print(f"Новый рейтинг: {rat}")
else:
    print("Ошибка. Вы ввели отрицательное число")
