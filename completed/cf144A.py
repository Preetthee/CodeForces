t = int(input())
arr = list(map(int, input().split()))
m,n = max(arr),min(arr)
mi,ni = arr.index(m)+1,len(arr) - 1 - arr[::-1].index(n)+1
if mi<ni:
    print(mi-1+t-ni)
else:
    print(mi-1+t-ni-1)
