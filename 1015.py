"""
import math
x1,y1 = list(map(float,input().split()))
x2,y2 = list(map(float,input().split()))
#d = ((x2-x1)**2+(y2-y1)**2)**0.5
d = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
print(f'{d:.4f}')
"""

from builtins import input
import math
a1, b1 = list(map(float,input().split()))
a2, b2 = list(map(float,input().split()))
#d = ((a2-a1)**2 + (b2-b1)**2)**0.5
d = math.sqrt(pow((a2-a1),2)+pow((b2-b1),2))
print(f'distance is {d:.4f}')

