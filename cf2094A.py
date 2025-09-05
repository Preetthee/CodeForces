n = int(input())
arr = []
for i in range(n):
    arr = input().split()
    first = arr[0][0]+arr[1][0]+arr[2][0]
    print(first)