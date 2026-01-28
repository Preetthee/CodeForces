t = int(input())

for _ in range(t):
    n = int(input())
    c = 0
    ind = 0
    s = input()
    ss = list(map(str,set(s)))
    ssl = len(ss)
    for i in range(ssl):
        if s.count(ss[i]) >= c:
            c == s.count(ss[i])
    out = len(s)-c
    print(out,ss[i])
