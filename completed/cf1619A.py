t = int(input())
for _ in range(t):
    s = input()
    if int(len(s))%2!=0:
        print("NO")
    elif s[:int(len(s)/2)]==s[int(len(s)/2):]:
        print("YES")
    else:
        print("NO")