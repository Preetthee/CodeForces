t = int(input())
for i in range(t):
    a,b = input().split()
    x,y = f"{b[0]}{a[1:]}",f"{a[0]}{b[1:]}"
    print(x,y)