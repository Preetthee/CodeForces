t = int(input())
for _ in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    m.sort()
    bm = len(m)
    lm = len(set(m))
    if bm == lm:
        print("YES")
    else:
        print("NO")