arr = list(map(int, input().split()))
arr = sorted(arr)
a,b,c = arr
print(((a-b)+(b-c))*-1)