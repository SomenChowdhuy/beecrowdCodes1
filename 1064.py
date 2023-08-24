c = 0
s = 0
for i in range(6):
    
    x = float(input()) 
    if(x<0):
        s = s+x
        c = c+1
avg = s/c
print(f'''{c} valores negatives
{avg:.1f}''')

