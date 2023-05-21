ticket = input('Введите номер билетика: ')
num1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
num2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
if num1 == num2:
    print('YES')
else:
    print('NO')

