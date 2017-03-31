import  math
print('ЗАДАНИЕ № 3')
def my_function(x,b,a,y):
    return (math.sqrt(x + b - a ) + math.log10(y)) / (math.atan(b + a))
print('Ответ:',my_function(2,2,2,2))