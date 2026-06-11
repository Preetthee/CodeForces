n = int(input())
arr = list(map(int, input().split()))
if len(set(arr))==1:
    print(-1)
else:
    print(*sorted(arr))