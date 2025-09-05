t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    if arr[0] == arr[1]:
        print(arr[2])
    elif arr[1] == arr[2]:
        print(arr[0])
    else:
        print(arr[1])