N1, N2, N3, N4 = list(map(float,input().split()))
avg1 = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1)/ (2+3+4+1) 
print(f'Media: {avg1:.1f}')
if avg1 >= 7.0: print('Aluno aprovado.')
elif avg1 < 5.0: print('Aluno reprovado.')
else: 
    print('Aluno em exame.')
    N5 = float(input()) 
    print(f'Nota do exame: {N5}')
    avg2 = (N5 + avg1)/2
    if avg2 >= 5: print('Aluno aprovado.')
    elif avg2 <= 4.9: print('Aluno reprovado.')
    print(f'Media final: {avg2:.1f}')
