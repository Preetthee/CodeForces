t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    c,s = 1,0
    for i in arr:
        if c %2 != 0:
            s+=i
        else:
            s-=i
        c+=1
    print(s)