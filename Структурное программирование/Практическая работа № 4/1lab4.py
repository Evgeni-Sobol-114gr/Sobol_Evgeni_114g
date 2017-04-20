import math
n = int(input("Введите N:"))
a = float(input("Введите A:"))
b = float(input("Введите B,(A < B): "))
if a < b:
    k = (b-a)/n
    print('F(',a,')= ',1-math.sin(a))
    for i in range(1,n+1):
        a = a + k
        print('F(',a,')= ',1-math.sin(a))
    print('F(', b, ')= ', 1 - math.sin(b))
else:
    print("Введите A<B")


