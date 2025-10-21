n = int(input())
arr = list(map(int, input().split()))
se = 0
di = 0
c = 1
while True:
    tempArr = [arr[0],arr[-1]]
    if c%2 != 0:
        se+=max(tempArr)
    else:
        di+=max(tempArr)
    arr.remove(max(tempArr))
    c+=1
    if arr == []:
        print(se,di)
        break