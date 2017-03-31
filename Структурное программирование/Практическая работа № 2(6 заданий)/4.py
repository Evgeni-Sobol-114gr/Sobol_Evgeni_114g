import  math
print('ЗАДАНИЕ № 4')
print("Введите основания трапеции a>b: ")
a = int(input("Введите А: "))
b = int(input("Введите В: "))
if (a>b) and (b>0):
    print("Введите угол альфа: ")
    al = int(input("Введите острый угол: "))
    if (al > 0) and (al < 90):
        al = (al * 3.14)/180
        h = (a - b) * math.sin(al) / (2 * math.cos(al))
        s = ((a+b)*h)/2
        print("S=",s)
    else: print("Введён не верный угол!")
else: print("Введёны неверные данные!")