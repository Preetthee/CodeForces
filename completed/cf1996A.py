t = int(input())
for t in range(t):
    n = int(input())
    if (n-2)%4 == 0:
        print(int(((n-2)/4)+1))
    elif (n%4)==0:
        print(int(n/4))
    else:
        print(int(n/2))