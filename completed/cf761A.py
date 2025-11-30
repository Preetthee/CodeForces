a,b = map(int,input().split())
if a==0 and b == 0 :
    print("NO")
elif abs(a-b)==1 or abs(a-b)==0:
    print("YES")
else:
    print("NO")