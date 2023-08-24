N = int(input()) 
for i in range(1,N+1):
    X = int(input())
    if X==1:
        print(f'Not prime')
    if X>1:
        for i in range(2,X):
            if(X % i==0): 
                print(f'{X} nao eh primo')
                break
        else:
            print(f'{X} eh primo')