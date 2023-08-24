#empty list creation
rabbit = []
rat = []
frog = []

#input test case
N = int(input()) 
for i in range(N):
    amount,type = input().split()
    amount = int(amount) 
    if 1<=amount<=15:
        if type =='C':
            rabbit.append(amount)
        if type == 'R':
            rat.append(amount) 
        if type == 'S':
            frog.append(amount) 
#no of. each total
t_rabbit = sum(rabbit)
t_rat = sum(rat) 
t_frog = sum(frog)
#total animal
t_ani = t_rabbit + t_rat + t_frog
#percentage of each animal
p_rabbit = (t_rabbit/t_ani)*100
p_rat = (t_rat/t_ani)*100
p_frog = (t_frog/t_ani)*100
print(f'''Total: {t_ani} cobaias
Total de coelhos: {t_rabbit}
Total de ratos: {t_rat}
Total de sapos: {t_frog}
Percentual de coelhos: {p_rabbit:.2f} %
Percentual de ratos: {p_rat:.2f} %
Percentual de sapos: {p_frog:.2f} %''')




"""
C = 0
R = 0
S = 0
N = int(input()) 
for i in range(N):
    a, ch = input().split()
    a = int(a)
    if 1<=a<=15:
        if ch=='C':
            C = C+a 
        if ch=='R':
            R = R+a 
        if ch=='S':
            S = S+a 
t_amount = C+R+S
P_rabbit = (C/t_amount)*100
P_rat  = (R/t_amount)*100
P_frog = (S/t_amount)*100
print(f'''Total: {t_amount} cobaias
Total de coelhos: {C}
Total de ratos: {R}
Total de sapos: {S}
Percentual de coelhos: {P_rabbit:.2f} %
Percentual de ratos: {P_rat:.2f} %
Percentual de sapos: {P_frog:.2f} %''') 
"""