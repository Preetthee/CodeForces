import math
n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    if math.sqrt(i)%1 == 0 and i>3:
        print("YES")
    else:
        print("NO")