t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    m = (a*60)+b
    r = (24*60)-m
    print(r)