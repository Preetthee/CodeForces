n,m = map(int, input().split())
p250 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,51]
if p250[p250.index(n)+1] == m:
    print("YES")
else:
    print("NO")
