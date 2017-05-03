a = []
m = []
k=0
max1=-32000;
for i in range(5):
    a.append([])
    for j in range(5):
        print("Введите элемент двумерного массива а[",i,"],[",j,"]: ")
        k=float(input())
        a[i].append(k)
        if max1 < abs(k): max1=k
print("------------------------------------")
print("Исходный массив: ")
for r in a:
    print(r)
print("------------------------------------")
print("Максимальный элемент: ",max1)
print("------------------------------------")
for i in range(5):
    m.append([])
    for j in range(5):
        k = a[i][j]/max1
        m[i].append(k)
print("Переделанный массив:")
for r in m:
    print(r)
