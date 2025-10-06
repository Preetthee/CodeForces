n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    out = 0
    if b%2 == 0:
        out = ((b*(2**(a-1))-1))/3
    else:
        out = b*(2**a)
    print(int(out))