for i in range(int(input())):
    n = int(input())
    s = input()
    c=0
    for i in range(n):
        if s[i]!=s[-i-1]:
            c+=1
        else:
            break
    if n-c*2<0:
        print(0)
    else:
        print(n-c*2)