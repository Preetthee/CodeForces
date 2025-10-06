t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    if a>=b:
        print(a)
    else:
        if (b-((b-a)*2))<=(b-(b-a)):
            print(a-(b-a))
        else:
            print(0)