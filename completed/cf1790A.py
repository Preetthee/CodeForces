t = int(input())
pi30 = "314159265358979323846264338327"
for _ in range(t):
    n = input()
    c = 0
    for i in range(len(n)):
        if pi30[i] == n[i]:
            c+=1
        else:
            break
    print(c)
