s = input()
t = input()
s = sorted(s)
t = sorted(t)
vs = s.count("a")+s.count("e")+s.count("i")+s.count("o")+s.count("u")
cs = len(s)-vs
vt = t.count("a")+t.count("e")+t.count("i")+t.count("o")+t.count("u")
ct = len(t)-vt
if vs == vt and cs == ct:
    print("Yes")
else:
    print("No")