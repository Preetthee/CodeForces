t = int(input())
for _ in range(t):
    s = input()[::-1].replace("p","-")
    s = s.replace("q","p")
    s = s.replace("-","q")
    print(s)
    