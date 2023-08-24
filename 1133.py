"""
X = int(input()) 
Y = int(input())
Min = min(X,Y)
Max = max(X,Y)
if X<Y:
    for i in range(Min+1,Max):
        if i%5==2 or i%5==3:
            print(f'{i}') 
else:
    if X>Y:
        for i in range(Max+1,Min):
            if i%5==2 or i%5==3:
                print(f'{i}')
"""
X = int(input())
Y = int(input())
Max = max(X,Y)
Min = min(X,Y)
for i in range(Min+1,Max):
    if i % 5 == 2 or i % 5 == 3:
        print(f'{i}')