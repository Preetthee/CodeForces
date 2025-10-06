t = int(input())

for _ in range(t):
    s = input()
    s1 = f"{s[1]}{s[0]}{s[2]}"
    s2 = f"{s[0]}{s[2]}{s[1]}"
    s3 = f"{s[2]}{s[1]}{s[0]}"
    if s1 == "abc" or s2 == "abc" or s3 == "abc" or s == "abc":
        print("YES")
    else:
        print("NO")