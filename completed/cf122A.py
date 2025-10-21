n = input()
if int(n)%4 == 0 or int(n)%7 == 0:
    print("YES")
elif "1" not in n or "2" not in n or "3" not in n or "5" not in n or "6" not in n or "8" not in n or "9" not in n:
    print("YES")
else:
    print("NO")