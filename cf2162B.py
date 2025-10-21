t = int(input())
for _ in range(t):
    n = input(int())
    b = input()
    c = 0
    a = []
    if b == "0":
        print("0\n")
    elif "0" in b:
        while True:
            c+=1
            a = a.append(b[b.index("0")])
            print(a)
            break
    else:
        print("0\n")