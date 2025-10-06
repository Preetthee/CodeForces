t = int(input())
for _ in range(t):
    x,n = map(int,input().split())
    s = 0
    for i in range(1,n+1):
        if i%2 != 0:
            s+=x
        else:
            s-=x
    print(s)