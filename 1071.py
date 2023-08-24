X = int(input())
Y = int(input())
s = 0
for i in range(X-1,Y,-1):
    if i%2!=0:
        s = s+i
print(f'{s}')