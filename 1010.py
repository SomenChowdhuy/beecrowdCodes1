from builtins import input

'''
x = input().split(' ')[1:]
y = input().split(' ')[1:]
total = int(x[0])*float(x[1]) + int(y[0])*float(y[1])
print(f'VALOR A PAGAR: R$ {total:.2f}')
'''

'''
#x = [int(x) for x in input().split(' ')[1:]]
x = 'odd'
print('x is odd') if x == 'odd' else print('x is even')
'''
'''
x = 'gdegdgd'
print('x is odd') if x == 'odd' else print('x is even')
'''
'''
b = '12.1'
print('.' in b)
'''
'''
x = '121'
print('.' in x)
'''


'''
x = [float(x) if '.' in x else int(x) for x in input().split(' ')[1:]]
y = [float(y) if '.' in y else int(y) for y in input().split(' ')[1:]]
val_to_pay = x[0]*x[1] + y[0]*y[1]
print(f'VALOR A PAGAR: R$ {val_to_pay:.2f}')
'''

'''
x = "1001"
print(x.isdigit())

y = '100.50'
print(y.isdigit())
'''

x = [int(x) if x.isdigit() else float(x) for x in input().split(' ')[1:]]
y = [int(y) if y.isdigit() else float(y) for y in input().split(' ')[1:]]
val_to_pay = x[0]*x[1] + y[0]*y[1]
print(f'VALOR A PAGAR: R$ {val_to_pay:.2f}')

