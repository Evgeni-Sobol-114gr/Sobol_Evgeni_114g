n = int(input("Сколько учеников в классе:"))
m=[]
sum=0
for i in range(1,n+1):
    r=int(input('Введите рост ученика: '))
    m.append(r)
k=len(m)
for i in range(1,k):
    sum=sum+m[i]
rez =float(sum/k)
print("Средний рост учеников: ",rez)