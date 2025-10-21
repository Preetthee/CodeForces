t = int(input())
mc,cc = 0,0
for _ in range(t):
    m,c = map(int, input().split())
    if m<c:
        cc+=1
    elif c<m:
        mc+=1
if mc<cc:
    print("Chris")
elif cc<mc:
    print("Mishka")
else:
    print("Friendship is magic!^^")