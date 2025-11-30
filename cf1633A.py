t = int(input())
for i in range(t):
    n,c = int(input()),0
    while True:
        n+=1
        c+=1
        if n%7 == 0 and n%10 !=0:
            break
    print(c)