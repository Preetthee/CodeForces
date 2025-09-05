n = int(input())
results = []
for i in range(n):
    l,r,d,u = map(int, input().split())
    if l==r==d==u:
        results.append("Yes")
    else:
        results.append("No")
print("\n".join(results))