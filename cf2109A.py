t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    if arr[0] == 1 and arr[1] == 1:
        print("YES")
    elif arr[0] == 0 and arr[1] == 0:
        print("YES")
    else:
        for i in range(2,n-1):
            if arr[i] == arr[i+1]:
                print("YES")
                break
            else:
                print("NO")