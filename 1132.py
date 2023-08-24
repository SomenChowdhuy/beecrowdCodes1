X = int(input())
Y = int(input())
s = 0
Min = min(X,Y)
Max = max(X,Y)
for i in range(Min,Max+1):
    if(i % 13!=0):
        s = s+i
print(f'{s}')