a,b = map(int, input().split())
st = 20*60
t = st+b
c = 0
for i in range(1,a+1):
    t+=i*5
    if t <= 24*60:
        c+=1
print(c)