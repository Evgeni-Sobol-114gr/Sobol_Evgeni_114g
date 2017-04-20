import  math
n= int(input("Введите количество N:"))
x=int(input("Введите x:"))
S=0
k=1
for i in range(1,n):
    k=k*2;
    S+=(x**k)/(math.factorial(k))
print(S)