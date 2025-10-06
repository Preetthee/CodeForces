import math
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    e,f = map(int,input().split())
    g,h = map(int,input().split())
    if a == c:
        D = math.sqrt(((c-a)**2)+((d-b)**2))
    elif a == e:
        D = math.sqrt(((e-a)**2)+((f-b)**2))
    else:
        D = math.sqrt(((g-a)**2)+((h-b)**2))
    print(int(D**2))