t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    if s.count("A") > s.count("B"):
        print("A")
    elif s.count("A") < s.count("B"):
        print("B")
    else:
        print("?")