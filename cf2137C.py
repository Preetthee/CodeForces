t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    o = 0
    if b==1:
        k = b
        o=(b/k)+(a*k)
    elif b%2!=0:
        if b>9:
            if b%9==0:
                k=b/9
                o=(b/k)+(a*k)
            elif b%7==0:
                k=b/7
                o=(b/k)+(a*k)
            elif b%5==0:
                k=b/5
                o=(b/k)+(a*k)
            elif b%3==0:
                k=b/3
                o=(b/k)+(a*k)
            elif b%1==0:
                k=b/1
                o=(b/k)+(a*k)
            else:
                o=-1
        else:
            for i in range(b,1,-1):
                if b%i==0:
                    k=i
                    o=(b/k)+(a*k)
                    break
                else:
                    k=b
                    o=(b/k)+(a*k)
    elif b%2==0:
            k=b/2
            o=(b/k)+(a*k)
    if o%2 == 0:
        print(int(o))
    else:
        print(-1)