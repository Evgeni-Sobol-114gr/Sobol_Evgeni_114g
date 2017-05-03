S1 =str(input('Введите строку:'))
d = len(S1)
for i in range(1,d-1):
    if S1[i] == '№':
        S1 = S1[1:i-1:1]+str(i)+S1[i+1:d:1]
print(S1)
