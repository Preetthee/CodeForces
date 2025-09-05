n = int(input())
for i in range(n):
    s = input()
    s2 = "codeforces"
    count = 0
    for i in range(len(s2)):
        if s[i] != s2[i]:
            count+=1
    print(count)