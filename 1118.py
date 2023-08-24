while True:
    valid = []
    while len(valid) < 2:
        x = float(input())
        if x>=0 and x<=10:
            valid.append(x)
        else:
            print(f'nota invalida')
    avg = sum(valid)/2
    print(f'media = {avg:.2f}')
    
    X = 0 
    while True:
        print(f'novo calculo (1-sim 2-nao)')
        X = int(input())
        if (X == 1) or (X == 2):
            break
    if X == 2:
        break 