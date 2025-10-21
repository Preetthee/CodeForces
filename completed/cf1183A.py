n = input()
while True:
    sumN = eval("+".join(n))
    m = int(n)+1
    n = str(m)
    if sumN%4 == 0:
        print(int(n)-1)
        break