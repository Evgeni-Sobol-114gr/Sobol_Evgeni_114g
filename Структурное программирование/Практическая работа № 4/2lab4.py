import math
k = int(input('Введите k:'))
sum1 = 0
pro1 = 1
for i in range(-3,k):
    if i != 5:
        sum1 += (math.pow(-1,i))/(math.pow((i-5),2))
for i in range(-3,2*k):
    pro1 *= (math.pow(i,3)-8)/(i+4)
print('W=',sum1+pro1)