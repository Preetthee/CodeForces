b,k = map(int, input().split())
arr = list(map(int, input().split()))
s = 0
c = 0
for i in range(len(arr)-1,-1,-1):
    s+=(arr[i])*(b**c)
    c+=1
if s%2 == 0:
    print("even")
else:
    print("odd")