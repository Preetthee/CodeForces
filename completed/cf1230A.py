b = list(map(int, input().split()))
b = sorted(b)
if (b[2]+b[1])==(b[3]+b[0]):
    print("YES")
elif (b[2]+b[1]+b[0])==b[3]:
    print("YES")
elif b[2]==b[1]==b[0]==b[3]:
    print("YES")
else:
    print("NO")