import random

print('На столе лежит 2021 конфета. За один ход можно забрать не более 28 конфет. Выигрывает тот, кто заберет последние конфеты.')
li = ['игрок A', 'игрок B']
who_first = random.choice(li)
if who_first == li[0]:
    who_second = li[1]
else:
    who_second = li[0]
print('Первый ход делает', who_first)
num_of_sweets = 2021
while num_of_sweets > 56:
    while True:
        print(f' \n{who_first}')
        move1 = int(input('Введите число конфет: '))
        try:
            
            if move1 <= 28 and move1 > 0:
                break
            else:
                print('По условию задачи введенное число не может быть больше 28 или меньше 0. Попробуйте еще раз.')
        except:
            print('Введите число еще раз:')
    num_of_sweets -=move1
    print('Осталось', num_of_sweets, 'конфет')
    while True:
        print(f' \n{who_second}')
        move2 = int(input('Введите число конфет: '))
        try:
            
            if move2 <= 28 and move2 > 0:
                break
            else:
                print('По условию задачи введенное число не может быть больше 28 или меньше 0. Попробуйте еще раз.')
        except:
            print('Введите число еще раз:')
    num_of_sweets -=move2
    print('Осталось', num_of_sweets, 'конфет')
print('')
print('Внимание! Осталось', num_of_sweets, 'конфет')

while num_of_sweets >0:
    while True:
        print(f' \n{who_first}')
        move1 = int(input('Введите число конфет: '))
        try:
            if (move1 <= 28 and move1 > 0) and num_of_sweets-move1>=0:
                break
            else:
                print('Попробуйте еще раз.')
        except:
            print('Введите число еще раз:')
    num_of_sweets-=move1
    if num_of_sweets==0:
        print('Выиграл', who_first)
    else:
        print('Внимание! Осталось', num_of_sweets, 'конфет')
        while True:
            print(f' \n{who_second}')
            move2 = int(input('Введите число конфет: '))
            try:
                if (move2 <= 28 and move2 > 0) and num_of_sweets-move2>=0:
                    break
                else:
                    print('Попробуйте ввести число конфет еще раз.')
            except:
                print('Введите число еще раз:')
        num_of_sweets-=move2
        if num_of_sweets==0:
            print('Выиграл',who_second)
        else:
            print('Внимание! Осталось', num_of_sweets, 'конфет')