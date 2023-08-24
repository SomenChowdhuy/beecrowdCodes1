from builtins import input


t_dist = int(input())
spent_fuel = float(input()) 
avg_consumption = (t_dist/spent_fuel)
print(f'{avg_consumption:.3f} km/l')