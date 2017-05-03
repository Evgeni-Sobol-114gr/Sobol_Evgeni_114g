k=int(input("Введите сколькизначное число у вас будет: "))
a=[]
m=[]
m1=[]
x2 = ''
S=0
S1=0
for i in range(1,k+1):
    x=int(input("Введите следующее число: "))
    if 0<= x <=1:
        x2 += str(x)
        a.append(x)
    else: print("Вводите можно 0 и 1! Начние заново!")
if len(a) == k:
      print("Исходое число: ",a)
      m1 = a[:k-1]
      x1 = str(a[len(a)-1])
      m.append(a[k-1])
      for i in range(0,len(m1)):
          x1 += str(m1[i])
          m.append(m1[i])
      print("Преобразованное число",m)
      l=0
      while l <= (k-1):
         if m[l] == 1:
             S=S+2**(k-l-1)
         l=l+1
      l=0
      while l <= (k - 1):
          if a[l] == 1:
              S1 = S1 + 2 ** (k-l-1)
          l = l + 1
      S=S+S1
      print("Ответ: ",bin(S))






