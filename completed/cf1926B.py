t = int(input())
for _ in range(t):
    n = int(input())
    m = []
    for i in range(n):
        s = input()
        if s.count("1") != 0:
            m.append(s.count("1"))
    if len(set(m)) == 1:
        print("SQUARE")
    else:
        print("TRIANGLE")