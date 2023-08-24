M, N = map(int,input().split())
while True:
    if M<=0 or N<=0:
        break
    else:
        Min = min(M,N)
        Max = max(M,N)
        li = []
        for i in range(Min,Max+1):
            li.append(i)
        sequence = ' '.join(map(str,li))
        res = sum(li)
        print(f'{sequence} Sum={res}') 
    M, N = map(int,input().split())
    