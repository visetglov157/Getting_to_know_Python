number = int(input('Введите трехзначное число: '))
if 100 < number < 999:
    a1 = number % 10
    a2 = number % 100 // 10
    a3 = number // 100
    print('Сумма цифр трехзначного числа равна:', a1 + a2 + a3)
else:
    print('Это не трехзначное число)')

