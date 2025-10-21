n = input()
ln = n[:len(n)-1:]
sln = n[:len(n)-2:]+n[-1]
arr = [int(n),int(ln),int(sln)]
print(max(arr))