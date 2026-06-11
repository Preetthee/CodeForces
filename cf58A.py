s = input()
for i in range(len(s)):
    if s[i]=="h":
        s = s[i:]
        print(s)
        break
