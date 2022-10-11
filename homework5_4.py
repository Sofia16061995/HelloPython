import random

def whoswin(list):
    if (list[0]=='O' and list[1]=='O' and list[2] == 'O') or (list[3]=='O' and list[4]=='O' and list[5]=='O') or (list[6]=='O' and list[7]=='O' and list[8]=='O') or (list[0]=='O' and list[4]== 'O' and list[8]=='O') or (list[2]=='O' and list[4]=='O' and list[6]=='O') or (list[0]=='O' and list[3]=='O' and list[6]=='O') or (list[1]=='O' and list[4]=='O' and list[7]=='O') or (list[2]=='O' and list[5]=='O' and list[8]=='O'):
        print('Компьютер выиграл')
        exit()
    elif(list[0]=='X' and list[1]=='X' and list[2] == 'X') or (list[3]=='X' and list[4]=='X' and list[5]=='X') or (list[6]=='X' and list[7]=='X' and list[8]=='X') or (list[0]=='X' and list[4]== 'X' and list[8]=='X') or (list[2]=='X' and list[4]=='X' and list[6]=='X') or (list[0]=='X' and list[3]=='X' and list[6]=='X') or (list[1]=='X' and list[4]=='X' and list[7]=='X') or (list[2]=='X' and list[5]=='X' and list[8]=='X'):
        print('Вы выиграли!')
        exit()

def printlist(list):
    for i in range(0, len(list), 3):
        print(list[i], list[i+1], list[i+2])

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Добро пожаловать в игру крестики-нолики. Перед собой вы видите поле с номерами позиций, которые в процессе игры будут заполняться крестиками или ноликами')
printlist(list)

x = int(input('Введите номер позиции, вместо которой Вы хотите поставить крестик: '))
list[x-1] = 'X'

printlist(list)

for i in range(4):
    print('\n'+ 'Xoд компьютера: ')
    o =-1
    while True:
        o = random.randint(1,9)
        try:
            int(list[o-1])
            list[o-1] = 'O'
            printlist(list)
            break
        except:
            o+=1
    whoswin(list)
    while True:
        print('')
        x = int(input('Введите номер позиции, вместо которой Вы хотите поставить крестик: '))
        try:
            int(list[x-1])
            list[x-1] = 'X'
            printlist(list)
            break
        except:
            print('Такая позиция уже занята. ')
    whoswin(list)