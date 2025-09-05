t = int(input())

for i in range(t):
    n = int(input())
    a = input()
    m = int(input())
    b = list(input())
    c = list(input())
    for i in range(m):
        if c[i] == "V":
            a = f"{b[i]}" + a
        elif c[i] == "D":
            a = a + f"{b[i]}"
    print(a)