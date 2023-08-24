#d1 = int(input().split()[-1])
dia,d1=input().split()
d1 = int(d1)
h1, m1, s1 = map(int,input().split(':'))
#d2 = int(input().split()[-1]) 
dia,d2 = input().split()
d2 = int(d2)
h2, m2, s2 = map(int,input().split(':'))
s = s2 - s1
h = h2 - h1 
m = m2 - m1 
d = d2 - d1
if s<0:
    s = s+60
    m = m - 1
if m<0:
    s+=60
    h = h-1
if h<0:
    h = h+24
    d = d-1
print(f'''{d} dia(s)
{h} hora(s)
{m} minuto(s)
{s} segundo(s)''')
