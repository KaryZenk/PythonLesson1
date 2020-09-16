print('Введите ваш вес')
a = int(input())
print('Введите ваш рост')
b = int(input())
c = a//((b/100)*(b/100))
c = int(c)
print('Ваш индекс массы тела ' + str(c))
scale = '15' + "=" * (c-15) + '|' + "="*(35 - (20 -c)) + "50"
print(scale)
