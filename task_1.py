# Пример 1
# def f(x):
#     x**2
# print(type(f))

# g = f
# print (f(1))
# print (g(1))

##Пример 2
# def f(x):
#     return x**2

# print (f(2))

### Пример 3
# def calc1(x):
#     return x+10
# def calc2(x):
#     return x*10

# def math(op, x):
#     print(op(x))

# math(calc1, 10)
# math(calc2, 10)

####Пример4
# def sum(x, y):
#     return x+y
sum = lambda x, y: x+y # тоже самое, что на 29 и 30 строчке

def mult(x, y):
    return x*y

def calc(op, a, b):
    print(op(a, b))

calc(mult, 4, 4)
calc(sum, 4, 4)

