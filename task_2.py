# list = []

# for i in range(1, 101):
#     if i%2 == 0:
#         list.append(i)
# print(list)

# list = [(i, i) for i in range(1, 21) if i%2 == 0]
# print(list)

def f(x):
    return x**3

list = [f(i) for i in range(1, 21) if i%2 == 0]
print(list)

#Задание 
path = 'C:/Users/Dmitriy/Desktop/Разработчик ГБ/8Знакомство с языком Python/Lections2.0/Lesson_3/filee.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != ' ':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1]

out = []
for e in numbers:
    if not e%2:
        out.append((e, e**2))
print (out)