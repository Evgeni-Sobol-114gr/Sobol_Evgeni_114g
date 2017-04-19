import math
x = int(input("Введите x: "))
if math.fabs(x) > 1:
    a = math.pow((math.sin(math.pow(x,3))),2)
    print("""Ответ: при |x|>1 """,a)
if math.fabs(x) <= 1:
    a = math.sqrt((6 * math.asin(math.pow(x,7)) + (4.5 * math.pow(x,6)) + (4* math.pow(x,2))+2))
    print("""Ответ: при |x|<=1 """, a)