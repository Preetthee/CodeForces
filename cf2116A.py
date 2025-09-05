t = int(input())

for i in range(t):
    a,b,c,d = map(int, input().split())
    a,c = sorted([a,c])
    b,d = sorted([b,d])

    jellyMax = a
    flowerMax = b

    if jellyMax < flowerMax:
        print("Flower")
    else:
        print("Gellyfish")