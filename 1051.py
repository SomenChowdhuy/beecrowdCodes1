'''
x = float(input()) - 2000
if x <= 0:
    print('Isento')
elif x<=1000:
    tax = ((x*8)/100)
    print(f'R$ {tax:.2f}') 
elif x<= 2500:
    tax = ((1000*8)/100) + (((x-1000)*18)/100)
    print(f'R$ {tax:.2f}')
else:
    tax = ((1000*8)/100) + ((1500*18)/100) + ((x-2500)*28)/100
    print(f'R$ {tax:.2f}')
'''

x = float(input())-2000
if x<=0:
    print('Isento')
elif x<=1000:
    tax = (x*8)/100
elif x<=2500:
    tax = (1000*8)/100 + ((x-1000)*18)/100
else:
    tax = (1000*8)/100 + (1500*18)/100 + ((x-2500)*20)/100
print(f'R$ {tax:.2f}')