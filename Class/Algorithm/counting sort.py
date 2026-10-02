arr = list(map(int, input().split()))

arr1 = [0]*(max(arr)+1)

arr2 = arr1.copy()

for i in range(len(arr2)):
    arr2[i] = arr.count(i)

arr3 = [0]*len(arr2)
c = 0
for i in range(len(arr3)):
    c += arr2[i]
    arr3[i]+=c

arrO = [0]*(len(arr))

for i in range(len(arr),0,-1):
    arrO = 

print(arr1,arr2,arr3,arrO)