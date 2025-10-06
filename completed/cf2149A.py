t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    c = 0
    z = arr.count(0)
    m1 = arr.count(-1)
    if m1%2 !=0:
        c+=2
    c+=z
    print(c)