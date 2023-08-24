N = int(input()) 
for i in range(1,N+1):
    X = int(input())
    if(X>0):
        if(X%2!=0):
            print('ODD POSITIVE')
        else:
            print('EVEN POSITIVE')
    elif(X<0):
        if(X%2!=0):
            print('ODD NEGATIVE')
        else:
            print('EVEN NEGATIVE')
    else:
        print('NULL')