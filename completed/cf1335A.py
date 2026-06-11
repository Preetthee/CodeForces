n = int(input())
for i in range(n):
    m = int(input())
    if m==1 or m==2:
        print(0)
    elif m%2==0:
        print(m//2-1)
    else:
        print(m//2)