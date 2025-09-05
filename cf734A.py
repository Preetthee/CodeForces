x = int(input())
y = input()
countA=0
countD=0
for i in y:
    if i == "A":
        countA+=1
    else:
        countD+=1
if countA > countD:
    print("Anton")
elif countA == countD:
    print("Friendship")
else:
    print("Danik")