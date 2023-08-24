curr_sal = float(input())
if curr_sal<=400: percentage = 15
elif curr_sal>400 and curr_sal<=800:  percentage = 12
elif curr_sal>800 and curr_sal<=1200: percentage = 10
elif curr_sal>1200 and curr_sal<=2000: percentage = 7
elif curr_sal>2000: percentage = 4
earn = (curr_sal*percentage)/100
new_sal = curr_sal + earn
print(f"""Novo salario: {new_sal:.2f}
Reajuste ganho: {earn:.2f}
Em percentual: {percentage} %""")
    