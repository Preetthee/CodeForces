t = int(input())

for i in range(t):
    a,b = map(int, input().split())
    arr = []
    for j in range(a,b):
        arr.append((j-a)+(b-j))
    if arr == []:
        arr.append(0)
    min = sorted(arr)[0]
    print(min)