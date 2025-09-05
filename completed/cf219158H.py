import math

a,b = map(float, input().split())

floor = int(a/b)

if a==b:
    celi = int(a/b)
else:
    celi = int(a/b)+1

if int(((a/b)%1)*10) > 4:
    round = int(a/b)+1
else:
    round = int(a/b)

print(f"floor {a:.0f} / {b:.0f} = {floor:.0f}\nceil {a:.0f} / {b:.0f} = {celi:.0f}\nround {a:.0f} / {b:.0f} = {((round))}")