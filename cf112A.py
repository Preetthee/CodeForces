x = input()
y = input()
num = [x,y]
num.sort(key=str.lower)
a,b = num
if x.lower() == y.lower():
    print(0)
elif x.lower() != y.lower():
    if a == x:
        print(-1)
    elif a == y:
        print(1)