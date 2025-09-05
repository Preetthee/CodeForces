n = input()
count = 0
for char in n:
    if char.isupper():
        count+=1
if len(n) < count*2:
    n = n.upper()
elif len(n) > count*2:
    n = n.lower()
elif len(n) == count*2:
    n = n.lower()
print(n)