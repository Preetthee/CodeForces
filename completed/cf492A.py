n = int(input())
s,d,c = 0,0,0
if n == 1 or n == 2:
    print(1)
else:
    for i in range(n):
        iS = int((i*(i+1))/2)
        s+=iS
        if s<n:
            c+=1
        elif s == n:
            print(c)
            break
        else:
            print(c-1)
            break