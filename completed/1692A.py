t = int(input())
for _ in range(t):
    a,b,c,d = map(int, input().split())
    l = [a,b,c,d]
    l = sorted(l,reverse=True)
    n = l.index(a)
    print(n)