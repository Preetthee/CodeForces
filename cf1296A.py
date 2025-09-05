t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    odd = 0
    even = 0
    for i in arr:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    if even == len(arr):
        print("NO")
    elif odd == (len(arr)) and odd%2 == 0:
        print("NO")
    else:
        print("YES")
        
    