t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr,reverse=True)
    c = 0
    for i in range(arr[0]+1):
        dup = arr.count(i)
        if dup == 2:
            c+=1
        elif dup>2 and dup%2 == 0:
            c+=(dup/2)
        elif dup>2 and dup%2 != 0:
            c+=((dup-1)/2)
    print(int(c))