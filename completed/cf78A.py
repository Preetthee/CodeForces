a = input()
b = input()
c = input()
ac = a.count("a")+a.count("e")+a.count("i")+a.count("o")+a.count("u")
bc = b.count("a")+b.count("e")+b.count("i")+b.count("o")+b.count("u")
cc = c.count("a")+c.count("e")+c.count("i")+c.count("o")+c.count("u")
if ac == 5 and bc == 7 and cc == 5:
    print("YES")
else:
    print("NO")