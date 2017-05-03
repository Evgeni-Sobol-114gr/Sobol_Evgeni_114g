st=str(input("Введите предложение:"))
k=len(st)
l=0
if st[k-1] == 'р':
    l=1
for i in range(0,k-1):
    if (st[i] == 'р') and (((st[i+1] == ' ') or (st[i+1] == '.')) or (st[i+1] == ',')):
        l=l+1
print("Количество слов заканчивающихся на р:",l)