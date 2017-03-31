import  math
print('ЗАДАНИЕ № 2')
def my_function(y,n):
    return (math.pow(y,2) - 0.8 * y + math.sqrt(y)) / (23.1 * math.pow(n,2) + math.cos(n))
print('Ответ:',my_function(2,2))