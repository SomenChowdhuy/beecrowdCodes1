alcohol = 0
gasoline = 0
diesel = 0
while True:
    N = int(input())
    if(N==1):
        alcohol+=1
    if(N==2):
        gasoline+=1
    if(N==3):
        diesel+=1
    if(N==4):
        break
print(f'''MUITO OBRIGADO
Alcool: {alcohol}
Gasolina: {gasoline}
Diesel: {diesel}''')