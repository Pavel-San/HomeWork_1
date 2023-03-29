def calc_sum(*nums):
    sum = 0
    symbol = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            symbol = True
    return sum, symbol

general_sum = 0

while True:
    numbers_string = input('Введите числа через пробел: ').split(' ')
    sum, stop_symbol = calc_sum(*numbers_string)
    general_sum += sum
    print(f'сумма {general_sum}')

    if stop_symbol:
        break
