highest = 0
pos = 0 
for i in range(100):
    N = int(input())
    if N>highest: 
        highest = N
        pos = i+1
print(f'''{highest}
{pos}''')