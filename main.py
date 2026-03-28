num = int(input('Введите количество чисел Фибоначчи в последовательности: '))
spisok = [1, 1]
if num > 2:
    for i in range(num - 2):
        a = spisok[-2] + spisok[-1]
        spisok.append(a)
    print(f'Последовательность чисел Фибоначчи: {spisok}')
elif num == 2:
    print(f'Последовательность чисел Фибоначчи: {spisok}')
else:
    print('Введите число побольше.')