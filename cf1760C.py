for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    sortedArr = sorted(arr)
    arre = []
    for i in arr:
        if i==sortedArr[-1]:
            arre.append(i-sortedArr[-2])
        else:
            arre.append(i-sortedArr[-1])
    print(*arre)
