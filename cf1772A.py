t = int(input())

for i in range(t):
    s = input()
    s = s.replace("+"," ")
    a,b = map(int, s.split())
    print(a+b)