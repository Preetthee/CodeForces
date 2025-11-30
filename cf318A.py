n,k = map(int,input().split())
s = 0
if n%2 == 0:
    o,e = int(n/2),int(n/2)
else:
    o,e = int((n+1)/2),int((n-1)/2)
if k>o:
    s = (k-o)*2
elif k<=o:
    s = (k*2)-1
print(s)