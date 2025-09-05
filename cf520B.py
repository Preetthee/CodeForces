m,n = map(int,input().split())
temp_m = m

if n%2!=0:
    count = 0
    while True:
        temp_m*=2
        big = temp_m
        count+=1
        print(count)
        if temp_m>n:
            break
    if m>n:
        print(m-n)
    else:
        print((big-n)+count)

else:
    if ((n/2)-m) <= 0:
        print(int((m-(n/2))+1))
    elif ((n/2)-m) >= 0:
        print(int(n/m))