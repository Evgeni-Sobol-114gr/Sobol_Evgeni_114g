m = []
i = 1
s = 1
otr = 0
nul = 0
for i in range(1,16):
    print("Введите ",i," элемент массива")
    a=int(input())
    m.append(a)
for i in range(0,15):
    if m[i] < 0:
        otr=otr+1
    if m[i] > 0:
        s=s*m[i]
    if m[i] == 0:
        nul=nul+1
print('---------------------------------------------')
print("Нулевых элементов: ",nul)
print("Отрицательных элементов: ",otr)
print("Произведение положительных элементов:",s)


