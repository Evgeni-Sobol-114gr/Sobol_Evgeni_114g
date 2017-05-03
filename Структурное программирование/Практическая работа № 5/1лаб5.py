S1 =str(input('Введите строку:'))
D= len(S1)
if D < 25:
    for i in range(D,25):
        S1+='_'
print(S1)