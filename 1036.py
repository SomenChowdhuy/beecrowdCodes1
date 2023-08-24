a,b,c = list(map(float,input().split()))
p = b*b - 4*a*c
q = 2*a
m = (-b+p**0.5)
n = (-b-p**0.5)

if a==0 or p<0:
    print('Impossivel calcular')
else:
    x1 = m/q 
    x2 = n/q 
    print(f"""R1 = {x1:.5f}
R2 = {x2:.5f}""") 
    
