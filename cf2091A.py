x = int(input())
date = [0,1,0,3,2,0,2,5]
for i in range(x):
    y = int(input())
    digits = map(int, input().split())
    for j in range(y):
        count = 1
        if digits[count] != date[count]:
            count+=1
print(count)