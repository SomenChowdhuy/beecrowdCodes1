from builtins import input

x = int(input())
y = x // 365
d = x % 365
m = d // 30 
d = d % 30 
print(f'''{y} ano(s)
{m} mes(es)
{d} dia(s)''')