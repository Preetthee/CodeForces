m,n,a = map(int, input().split())
x = m/a
x = int(x)
if m%a != 0:
    x+=1
y = n/a
y = int(y)
if n%a != 0:
    y+=1
z = x*y
print(int(z))