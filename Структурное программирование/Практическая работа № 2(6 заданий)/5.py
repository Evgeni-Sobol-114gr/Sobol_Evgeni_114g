import math
print('ЗАДАНИЕ № 5')
t = float(input('Введите t:'))
x = 0.9
b = (math.log10(math.fabs(x))) ** 2
a = t * x + math.sqrt(math.fabs(b))
y = math.pow(math.cos(a+ math.pow(b,3)),3)
print("Ответ:",y)