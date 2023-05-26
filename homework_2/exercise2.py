x = int(input('Первое загаданное число: '))
y = int(input('Второе загаданное число: '))
for A in range(x):
    for B in range(y):
        if x == A + B and y == A * B:
            print(A, B)




