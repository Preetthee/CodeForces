t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    arr = input()
    arrO = "+"*a
    top = arr.count("0")
    arrO = arrO.replace("+","-",top)
    bottom = arr.count("1")
    arrO = arrO[::-1]
    arrO = arrO.replace("+","-",bottom)
    arrO = arrO[::-1]
    both = arr.count("2")
    for2 = arrO.replace("-","")
    
    print(arrO,for2)