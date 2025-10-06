t = int(input())
for t in range(t):
    n = int(input())
    m = input()
    if int(m) > 0:
        o = m.replace("0","")
    else:
        o = 0
    if int(o) != 1 or int(o) == 0:
        print("No")
    else:
        print("YES")