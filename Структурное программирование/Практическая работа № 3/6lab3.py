a=input("Ведите четырёхзначное число:")
m=list(a)
if len(m) == 4:
    if (int(m[0])* int(m[1]) * int(m[2]) * int(m[3]))%3 == 0:
        print('Произведение цифр числа ',a ,' кратно 3.')
    else: print('Произведение цифр числа ',a ,' не кратно 3.')
else:
    print('Введите четырёхзначное')
if len(m) == 4:
    if (int(m[0])* int(m[1]) * int(m[2]) * int(m[3])) % 7 == 0:
        print('Произведение цифр числа ',a ,' кратно 7.')
    else: print('Произведение цифр числа ',a ,' не кратно 7.')
else:
    print('Введите четырёхзначное')
