li = list(map(int,input('Введите два числа через пробел: ').split()))
print(li)
a = lambda x, y: print(True) if x**2 ==y or y**2 ==x else print(False)
a(li[0],li[1])