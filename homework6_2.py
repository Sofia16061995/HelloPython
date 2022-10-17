
def inputNumber():
    return int(input("введите число N: "))

def factorial(x):
    f = lambda x: 1 if x == 0 else x * factorial(x - 1)
    return f(x)

def get_list(n):
    listFactorial = list(factorial(i) for i in range(1, n + 1))
    return listFactorial

print(get_list(inputNumber()))