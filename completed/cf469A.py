n = int(input())

arr1 = input().split()
if "0" in arr1:
    arr1.remove("0")
arr2 = input().split()
if "0" in arr2:
    arr2.remove("0")

arrAll = arr1[1:]+arr2[1:]

arrSet = set(arrAll)

size = len(arrSet)

if size == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")