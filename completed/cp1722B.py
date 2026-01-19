t = int(input())
for _ in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    for i in range(n):
        if s1[i] == "R" and s2[i] == "B":
            print("NO")
            c = 0
            break
        elif s1[i] == "B" and s2[i] == "R":
            print("NO")
            c = 0
            break
        elif s1[i] == "R" and s2[i] == "G":
            print("NO")
            c = 0
            break
        elif s1[i] == "G" and s2[i] == "R":
            print("NO")
            c = 0
            break
        else:
            c = 1
    if c == 1:
        print("YES")