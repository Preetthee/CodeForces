t,f = int(input()),0
for _ in range(t):
    s = input()
    match s[0]:
        case "T":
            f+=4
        case "C":
            f+=6
        case "O":
            f+=8
        case "D":
            f+=12
        case "I":
            f+=20
print(f)