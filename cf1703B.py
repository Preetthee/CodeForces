t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    sa = len(s)
    so = len(set(s))
    print((sa-so)+so*2)