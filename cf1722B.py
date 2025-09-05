t = int(input())

for i in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    same = "GB"
    for j in range(n):
        if s1[i] != s2[i]:
            if s1[i] in same and s2[i] in same:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")