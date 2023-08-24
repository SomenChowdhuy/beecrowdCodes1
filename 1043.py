A, B, C = map(float,input().split()) 
sum = A + B + C
area = 0.5*(A+B)*C
if A+B>C and A+C>B and B+C>A:
    print(f'Perimetro = {sum:.1f}')
else:
    print(f'Area = {area}') 