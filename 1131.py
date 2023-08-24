matches = 0
inter = 0
gremio = 0 
draw =  0
while True:
    I, G = map(int,input().split())
    if I>G:
        inter = inter+1
    elif G>I:
        gremio = gremio+1
    elif I==G:
        draw = draw+1
    matches = matches+1
    
    print(f"Novo grenal (1-sim 2-nao)") 

    check = int(input())
    if check == 2:
        break
print(f"""{matches} grenais
Inter:{inter}
Gremio:{gremio}
Empates:{draw}""")

if inter == gremio:
    print(f"Não houve vencedor")
else:
    if inter>gremio:
        print(f'Inter venceu mais')
    else:
        print(f'Gremio venceu mais')
            