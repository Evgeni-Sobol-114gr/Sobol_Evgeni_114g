n=int(input("Введите N:"))
m=int(input("Введите M:"))
for i in range(n):
    a.append([])
    for j in range(5):
        print("Введите элемент двумерного массива а[",i,"],[",j,"]: ")
        k=float(input())
        a[i].append(k)