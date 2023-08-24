"""
from builtins import input
x = int(input())
print(x)
for i in [100, 50, 20, 10, 5, 2 ,1]:
    print(f'{x//i} nota(s) de R$ {i},00')
    x = x % i 
"""
