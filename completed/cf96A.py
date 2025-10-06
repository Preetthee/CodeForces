s,f,c = input(),2,0
for i in s:
    if i == f:
        c+=1
    else:
        c=0
    f = i
    if c == 6:
        print("YES")
        break
else: 
    print("NO")