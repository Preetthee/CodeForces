for i in range(int(input())):
    n,a,b = list(map(int, input().split()))
    if b//3 > a:
        print(a*n)
    else:
        print(b*n)