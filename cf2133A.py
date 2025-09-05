t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    rev = 1
    for i in range(n):
        rev = arr[i]/arr[i+1] * rev