for _ in range(int(input())):
    s = input()
    ss = set(s)
    if len(ss) == 1:
        print("NO")
    else:
        s1 = s[0]
        s2 = s[1::]
        print(f"YES\n{s2+s1}")