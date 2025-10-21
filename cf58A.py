s = input()
st = s
hp = s.index("h")
s = s[hp::]
print(s)
ep = (s.index("e"))+hp
s = s[ep::]
print(s)
op = s.index("o")+hp
print(s)
if hp<ep<op and lc>=2:
    print("YES")
else:
    print("NO")