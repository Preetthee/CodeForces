t = int(input())

for i in range(t):
    n = int(input())
    sum = 0
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    for j in arr:
        if j <= 0:
            sum+=(j*-1)
        elif j >= 0:
            sum+=j
    print(sum)