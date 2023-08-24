even = 0
odd = 0
pos = 0
neg = 0
for i in range(5):
    x = float(input())
    if x % 2 == 0: even = even + 1
    else: odd = odd + 1
    if x > 0:   pos = pos + 1
    elif x < 0: neg = neg + 1
print(f'''{even} valor(es) par(es)
{odd} valor(es) impar(es)
{pos} valor(es) positivo(s)
{neg} valor(es) negativo(s)''')