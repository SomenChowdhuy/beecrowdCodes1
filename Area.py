
# 1st argument is function, 2nd argument is an iterable object
from builtins import input

"""
A,B,C = list(map(float,input().split()))    
pi = 3.14159
Triangle_Area = 0.5 * A * C
Circle_Area = pi*C**2
Trapezium_Area = 0.5*(A+B)*C
Square_Area = B**2
Rect_Area = A * B 
print(f'''TRIANGULO: {Triangle_Area:.3f}
CIRCULO: {Circle_Area:.3f}
TRAPEZIO: {Trapezium_Area:.3f}
QUADRADO: {Square_Area:.3f}
RETANGULO: {Rect_Area:.3f}''')
"""
x, y, z = list(map(float,input().split())) 
pi = 3.14159
t_area = 0.5 *x *z
c_area = pi*z**2
trap_area = 0.5*(x+y)*z
sq_area = y*y
rect_area = x**2
print(f"""Triangulo:{t_area:.3f}
Circulo:{c_area:.3f}""")
