t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = max(arr)
    av = (m*arr.count(m))/arr.count(m)
    print(int(av))