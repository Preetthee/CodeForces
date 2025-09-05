t = int(input())
out = ""

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sortedArr = sorted(arr)
    out+= f"{n}\n{sortedArr}\n"

