t = int(input())

for i in range(t):
    out = ""
    for i in range(8):
        s = input()
        s = s.replace(".","")
        if s != "":
            out+=s
    print(out)