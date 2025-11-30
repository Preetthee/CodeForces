n = int(input())
arr = list(map(int, input().split()))
max = max(arr)
max1 = max*2
max2 = max*3
max3 = max*2*3
arr.pop(arr.index(max))
c = 0
for i in arr:
    if max1%i == 0 and max2 % i == 0 and max3 % i == 0:
        c+=0
    else:
        c+=1
if c==0:
    print("YES")
else:
    print("NO")