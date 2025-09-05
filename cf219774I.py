import itertools

t = int(input())

for i in range(t):
    min = 0
    n = int(input())
    arr = list(map(int, input().split()))
    arrIJ = list(itertools.combinations(range(1,n+1),2))
    for j in range(len(arr)):
        i_val = arr[j][0] - 1
        k_val = arr[j][1] - 1
        eq = arr[(arr[j][0])-1]+arr[arr([j][1])-1]+arr[j][0]+arr[j][1]
    if min > eq:
        min+=eq
    print(min)