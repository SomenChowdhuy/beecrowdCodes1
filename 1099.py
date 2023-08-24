N = int(input()) 
for i in range(N):
    x, y = map(int,input().split()) 
    Max = max(x,y)
    Min = min(x,y) 
    s = 0
    for j in range(Min+1,Max):
        if (j%2)!=0:
            s = s+j
    print(f'{s}') 
"""
N = int(input()) 
for i in range(N):
    X, Y = map(int,input().split())
    Max = max(X,Y)
    Min = min(X,Y) 
    li =[] 
    for j in range(Min+1,Max):
        if(j%2!=0):
            li.append(j) 
    print(li) 
    s = sum(li) 
    print(s) 
"""