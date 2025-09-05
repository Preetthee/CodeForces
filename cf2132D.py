t = int(input())
for i in range(t):
    n = int(input())
    toSum = ""
    for i in range(1,n+1):
        toSum+=f"{i}"
    toSum2 = list(toSum[:n])
    sum = 0
    for i in toSum2:
        sum+= int(i)
    print(sum)