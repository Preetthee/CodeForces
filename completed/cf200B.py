n = int(input())
arr = list(map(int, input().split()))
s=0
for i in arr:
    s+=i
print(f"{s/n:.12f}")