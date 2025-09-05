n = int(input())
arr = list(map(int, input().split()))

for i in arr:
    indT = []
    try:
        ind1 = arr.index(1)
        print(ind1)
        arr = arr.pop[ind1]
    except:
        break
    print(indT)


