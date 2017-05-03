S1 =str(input('Введите строку:'))
d = len(S1)
m=[]
k=0
for i in range(0,d):
    if S1[i] not in m:
        m+=S1[i]
for i in range(0,len(m)):
    for j in range(0,d):
        if m[i]== S1[j]:
            k+=1
    print(m[i],'встретилось\n',k, 'раз')
    k=0
print(m)