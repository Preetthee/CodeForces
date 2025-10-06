t = int(input())
for _ in range(t):
    n = int(input())
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))
    arrC = []
    count = 0
    for i in range(n):
        if arrA[i] > arrB[i]:
            arrC.append((arrA[i] - arrB[i])+1)
        elif arrA[i] == arrB[i]:
            arrC.append(1)
        count+=1
    print(max(arrC),count)