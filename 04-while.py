''' x = 0

while x < 10:
    print(x)
    x=x+1
'''
sum = 0

a = int(input('ingrese el primer numero: '))
b = int(input('ingrese el segundo numero: '))
i = 0
res = ''

while (i != b):
    sum = sum + a
    res = res + f'{a}'
    i = i + 1
    if i != b:
        res = res + ' + '

print(res + f' = {sum}')
