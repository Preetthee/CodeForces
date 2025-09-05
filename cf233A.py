n = int(input())
arr = []
if n == 1:
    print(-1)
elif n%2 == 0:
    for i in range(1,n+1):
        if i%2 != 0:
            arr.append(i+1)
        else:
            arr.append(i-1)
else:
    arr.append(-1)
print(*arr)