"""
R = float(input())
pi = 3.14159
formula = pi*R**2
print(f"A={formula:.4f}")   f string # {} is called dynamic value
"""
from builtins import input


print('Hello',end=' ')
print('World') 

"""
R = float(input())
pi = 3.14159
res = pi*R**2
print(f'A={res:.3f}')
"""

"""
R = float(input())
pi = 3.14159
res = pi*R**2
print('S=%.4f'%res)
"""

"""
A = int(input())
B = int(input())
sum = A+B
print(f'res={sum}')
"""

"""
A = int(input())
B = int(input())
sum = A+B
print(f'SOMA = {sum}')
"""
"""
A = int(input())
B = int(input())
product = A*B
print(f'PROD = {product}')
"""
#print('MEDIA = {avg:.5f}')

"""
A = float(input())*2
B = float(input())*3
C = float(input())*5
avg = (A+B+C)/(2+3+5)
print(f'MEDIA = {avg:.1f}')
"""

"""
A = int(input())
B = int(input())
C = int(input())
D = int(input())
diff = A*B - C*D
print(f'DIFERENCA = {diff}') 
"""
"""
num = int(input())
hours = int(input())
amount = float(input())
print(f'NUMBER = {num}')
print(f'SALARY = U$ {(amount*hours):.2f}')
"""

"""
input()                       //input() function by default returns a string
fixed_salary = float(input())
bonus = (float(input())*15)/100
total = fixed_salary + bonus
print(f'TOTAL = R$ {total:.2f}')
#print('TOTAL = R$ %.2f'%total)
"""

"""
print('Bye',end=' ')
print('World')
"""
"""
num = int(input())
hours = int(input())
amount = float(input())
total = hours*amount
print(f'NUMBER = {num}')
print(f'SALARY = U$ {total:.2f}')
"""

"""
fixed_sal = float(input())
t_sale = float(input())
bonus = (t_sale*15)/100
total = bonus + fixed_sal
print(f'TOTAL = R$ {total:.2f}')
"""

#1010
#split() returns a list as a string for each items
"""
x = input().split(' ')[1:]  
y = input().split(' ')[1:]
val_to_pay = int(x[0])*float(x[1]) + int(y[0])*float(y[1])
print(f'VALOR A PAGAR: R$ {val_to_pay:.2f}')
"""

#1010
#List compreshension

"""
x = [int(x) for x in input().split(' ')[1:]]
print(x) 
"""
"""
x = [float(x) if '.' in x else int(x) for x in input.split()[1:]]
print(x) 
"""
# x = [float(x) if x.isdigit() else int(x) for x in input().split()[1:]]

"""
num = 20 
print(f'{num} is odd') if num == 'odd' else print(f'{num} is even')
"""
"""
num = int(input())
print(f'{num} is even') if num % 2 == 0  else print(f'{num} is odd')
"""

"""
print("Welcome",end='\n')
print('To Python') 
"""
"""
print("Welcome",end=' ')
print('To Python') 
"""
"""
print('Hello My dear',end='@')
print('Faryia')
"""
print('Python',end='@')
print('geeks for geeks')


print(int(570/100))


x = 100
print(type(x))

y = 12.40
print(type(y))

print(type(20))

print(type('Somen'))

num = 1220.5603
limit = round(num,2)
print(limit)

num = 600.4567
lim = '{.2f}'.format(num)
print(lim)

num = '1100.00'
print(num.isdigit())

# float(x) float built in function
# int(x) integer built in function