A, B = map(int,input().split())
if B % A == 0 or A % B == 0: print('Sao Multiplos')
elif B%A!=0: print('Nao sao Multiplos')