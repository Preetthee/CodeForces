for _ in range(int(input())):
    s = input()
    ls = len(s)
    for i in range(ls-1):
        if s[i]==s[i+1]:
            print(1)
            break
    else:
        print(ls)