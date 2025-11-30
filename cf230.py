n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    c = 0
    for j in range(1,i):
        if i%j==0:
            c+=1
    if c==2:
        print("YES")
    else:
        print("NO")