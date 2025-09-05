t = int(input())
for i in range(t):
    s = input()
    if ((s[0] == "Y" or s[0] == "y") and (s[1] == "E" or s[1] == "e") and (s[2] == "S" or s[2] == "s")):
        print("YES")
    else:
        print("NO")