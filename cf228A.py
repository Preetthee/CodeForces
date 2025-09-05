arr = list(map(int, input().split()))
if len(set(arr)) == 1:
    print(3)
if len(set(arr)) == 2:
    print(2)
if len(set(arr)) == 3:
    print(1)
if len(set(arr)) == 4:
    print(0)
