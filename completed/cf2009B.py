for _ in range(int(input())):
    arr = []
    for i in range(int(input())):
        s = input()
        arr.append(s.index("#")+1)
    print(*arr[::-1])