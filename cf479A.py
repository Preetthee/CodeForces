a = int(input())
b = int(input())
c = int(input())

A = a+b*c
B = a*(b+c)
C = a*b*c
D = (a+b)*c
E = a+b+c

arr = [A,B,C,D,E]

arr = sorted(arr)

print(arr[-1])