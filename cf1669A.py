n = int(input())
for i in range(n):
    a = int(input())
    if 1900 <= a:
        print("Division 1")
    elif 1600 <= a:
        print("Division 2")
    elif 1400 <= a:
        print("Division 3")
    else :
        print("Division 4")