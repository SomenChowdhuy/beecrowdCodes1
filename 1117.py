valid = []
while True:
    for i in range(1):
        score = float(input()) 
        if score>=0 and score<=10:
            valid.append(score)
        else:
            print(f'nota invalida')
    if len(valid) == 2:
        avg = sum(valid)/2
        print(f'media = {avg:.2f}')
        break