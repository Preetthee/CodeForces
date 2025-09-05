import math
n = int(input())
for i in range(n):
    x = int(input())
    sqrt = math.sqrt(x)
    if sqrt %1 == 0:
        if sqrt%2 == 0:
            y = sqrt/2
            z = sqrt/2
        else:
            y = (sqrt-1)/2
            z = (sqrt+1)/2
        print(f"{y:.0f} {z:.0f}")
    else:
        print(-1)