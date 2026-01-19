t = int(input())
for _ in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    c = 0
    for i in m:
        c+=i
    if (c**.5)%1 ==0:
        print("YES")
    else:
        print("NO")