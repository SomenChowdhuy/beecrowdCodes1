from builtins import input

"""
sec = int(input())
mint = sec//60
sec = sec % 60
hrs = mint//60
mint = mint % 60
print(f'{hrs}:{mint}:{sec}') 
#print(mint)
#print(sec)
#print(hrs)

"""
while True:
    x = int(input())
    h = x//3600
    sec = x % 3600
    min = sec // 60 
    sec = sec % 60
    print(f'{h}:{min}:{sec}')