p,q,r,s = map(int,input().split())
start = p * 60 + q 
end = r * 60 + s 
diff = end - start

if diff<=0:
    diff = diff + 24*60
    #diff1 = diff * 60

hrs = diff//60
min = diff % 60 
print(f'O JOGO DUROU {hrs} HORA(S) E {min} MINUTO(S)')
