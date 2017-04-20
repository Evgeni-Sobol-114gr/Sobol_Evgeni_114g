a = int(input("Введите a:"))
b = int(input("Введите b:"))
c = int(input("Введите c:"))
d = int(input("Введите d:"))
m =[a,b,c,d]
z = 0
p = 0
k = 0
for i in range(0,4):
    k = m[i]
    if ((k%3) == 0) and (p == 0):
        print(k,' делиться на 3')
        p = 1
    if ((k%5) == 0) and (z == 0):
        print(k, ' делиться на 5')
        z = 1


