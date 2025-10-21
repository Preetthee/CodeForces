t = int(input())
for i in range(t):
    a = input()
    b = input()
    c = input()
    if "?" in a:
        d = a
    elif "?" in b:
        d = b
    elif "?" in c:
        d = c
    d = d.replace("?","")
    d = sorted(d)
    if "A" not in d:
        print("A")
    elif "B" not in d:
        print("B")
    elif "C" not in d:
        print("C")