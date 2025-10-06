l1,r1,l2,r2 = map(int, input().split())

lDiff = l2 - l1
rDiff = r2 - r1

if r1<l2 or r2<l1:
    print(-1)
