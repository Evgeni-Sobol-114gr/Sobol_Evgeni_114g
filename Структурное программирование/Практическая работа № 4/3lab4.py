v=int(input("Введите N: "))
m=[]
z=0
for n in range(2,v):
    for i in range(2,n-1):
        if n%i == 0:
            z=1
    if (z==0) and (n!=2):
        m.append(n)
    z=0
k=len(m)
for i in range(1,k):
    if v%m[i] == 0:
        print('Найден простой делитель числа N:',m[i])






