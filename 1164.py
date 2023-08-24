"""
N = int(input())
for i in range(1,N+1):
    s = 0
    X = int(input())
    for j in range(1,X):
        if X % j == 0:
            #print(j,end=' ')
            s = s+j
    if s == X:
        print(f'{X} eh perfeito')
    else:
        print(f'{X} nao eh perfeito')
"""

s = 0
N = int(input()) 
for i in range(1,N):
    if N % i == 0:
        print(i,end=' ')
        s = s+i
print(end='\n')
if s == N: print(N,'is a perfect number')
else: print('\n',N,'is not a perfect number')