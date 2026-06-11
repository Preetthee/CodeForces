n = int(input())
s = 0
for i in range(500):
    s+=i
    if s == n:
        print("YES")
        break     
    elif s>n:
        print("NO")
        break