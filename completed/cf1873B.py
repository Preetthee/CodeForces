t = int(input())
for _ in range(t):
    c = 1
    n = int(input())
    m = list(map(int, input().split()))
    m = sorted(m)
    m[0] = m[0]+1
    for i in m:
        c*=i
    print(c)