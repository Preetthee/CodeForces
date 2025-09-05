a,b = map(int, input().split())
if a-b==1 or b-a==1:
    print("YES")
elif a==0 and b==0:
    print("NO")
elif a==b:
    print("YES")
else:
    print("NO")