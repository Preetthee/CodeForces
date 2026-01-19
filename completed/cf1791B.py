t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    m = [0,0]
    for i in s:
        if i == "U":
            m[1] = m[1]+1
        if i == "D":
            m[1] = m[1]-1
        if i == "R":
            m[0] = m[0]+1
        if i == "L":
            m[0] = m[0]-1
        if m == [1,1]:
            print("YES")
            c = 0
            break
        else:
            c = 1
    if c == 1:
        print("NO")
    