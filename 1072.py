N=int(input())
inn=0
out=0
#for i in range(N):
#for i in range(1,N+1):
for i in range(0,N):
    X = int(input())
    if X>=10 and X<=20:
        inn = inn + 1
    else:
        out+=1
print(f'''{inn} in
{out} out''')