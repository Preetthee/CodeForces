n,m = input().split()
for i in range(1,int(n)+1):
    if i%4==0:
        print("#"+"."*(int(m)-1))
    elif i%2==0:
        print("."*(int(m)-1)+"#")
    else:
        print("#"*(int(m)))