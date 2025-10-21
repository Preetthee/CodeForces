n = input()
x = ""
for i in n:
    if (9-int(i))<0:
        x+= f"{i}"
    else:
        x+= f"{9-int(i)}"
print(x)