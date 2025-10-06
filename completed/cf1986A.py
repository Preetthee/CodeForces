t = int(input())
for _ in range(t):
    a,b,c = map(int, input().split())
    s1 = abs(a-a)+abs(b-a)+abs(c-a)
    s2 = abs(a-b)+abs(b-b)+abs(c-b)
    s3 = abs(a-c)+abs(b-c)+abs(c-c)
    arr = [s1,s2,s3]
    print(min(arr))