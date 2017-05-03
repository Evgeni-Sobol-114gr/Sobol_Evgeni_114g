m=[]
loc=0
k = int(input("Введите количество элементов массива: "))
for i in range(1,k+1):
    print("Введите ",i," элемент: ")
    m.append(int(input()))
for i in range(1,k-1):
    sr=0
    niz=0
    verh=0
    niz=m[i-1]
    print(m[i-1])
    sr=sr+m[i]
    print(m[i])
    sr=sr+m[i+1]
    print(m[i + 1])
    sr=sr+m[i+2]
    print(m[i + 2])
    sr=sr/3
    verh=m[i+3]
    print(m[i + 3])
    if  (sr < verh) or (sr < niz):
        loc=loc+1
print(loc)


