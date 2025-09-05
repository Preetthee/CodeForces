t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.append(2)
    c = 0
    space = []
    for j in arr:
        if j == 0:
            c+=1
        if j == 1 or j == 2:
            space.append(c)
            c = 0          
    print(max(space))