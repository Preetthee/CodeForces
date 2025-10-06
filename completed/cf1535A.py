t = int(input())
for i in range(t):
    a,b,c,d = map(int,input().split())
    fp = a,b
    fp = sorted(fp)
    sp = c,d
    sp = sorted(sp)
    w = fp[1],sp[1]
    w = sorted(w)
    ap = a,b,c,d
    ap = sorted(ap)
    if w[0] == ap[2] and w[1] == ap[3]:
        print("YES")
    else:
        print("NO")