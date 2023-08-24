while True:
    X, Y = map(int,input().split()) 
    if X==Y:
        break
    if X > Y:
        print(f'Decrescente')
    else:
        print(f'Crescente')
        