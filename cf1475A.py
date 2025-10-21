t = int(input())
arr = [1,3,5,7,9]
for _ in range(t):
    n = int(input())
    if n%2 == 0:
        print("NO")
    elif n%3==0 or n%5==0 or n%7==0 or n%9==0:
        print("YES")
    else:
        print("NO")