from builtins import input

x = float(input())

print('NOTAS:')
for i in [100, 50, 20, 10, 5, 2]:
    print(f'{int(x//i)} nota(s) de R$ {i}.00')   # int() is input building function
    x = float(f'{x % i:.2f}')
#print(x)
#print(f'{x}')
#print(f'{x:.2f}')
#print(float(f'{x:.2f}')
# print(type(float(f'{x:.2f}'))) 
print('MOEDAS:')
for i in [1, 0.50, 0.25, 0.10, 0.05, 0.01]:
    print(f'{int(x/i)} moeda(s) de R$ {i:.2f}')
    x = float(f'{x % i:.2f}')
    
#exercise
m_val = float(input())
print('NOTAS:')
for i in [100, 50, 20, 10, 5, 2]:
    print(f'{int(m_val//i)} nota(s) de R$ {i}.00')  
    m_val = float(f'{m_val % i:.2f}')
print('MOEDAS:')
for i in [1, 0.50, 0.25, 0.10, 0.05, 0.01]:
    print(f'{int(m_val/i)} moeda(s) de R$ {i:.2f}')
    m_val = float(f'{m_val % i:.2f}')
#print(m)
#print(f'{x}')
#print(f'{x:.2f}')
#print(float(f'{x:.2f}'))
#print(type(float(f'{x:.2f}')))
    

