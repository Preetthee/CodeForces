t = int(input())
for _ in range(t):
    n = int(input())
    if n == 0:
        print(3)
    elif n%3 == 0:
        print(0)
    elif n%3 != 0:
        print((3-(n%3)))