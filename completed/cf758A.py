n =  int(input())
arr = list(map(int,input().split()))
arr = sorted(arr)
s = 0
for i in range(n-1):
    s+=arr[-1]-arr[i]
print(s)