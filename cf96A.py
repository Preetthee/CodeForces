x = input()
count = 0
ver = True
for i in range(len(x)-1):
    if x[i] == x[i+1]:
        count+=1
    else:
        count=0
    if count > 6:
        ver = True
        print(ver)
        break
    else:
        ver = False
        print(ver)
if ver == True:
    print("YES")
else:
    print("NO")