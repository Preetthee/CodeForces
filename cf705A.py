n = int(input())
feel = "I hate "

for i in range(n-1):
    feel+= "that "
    if i%2 == 0:
        feel+= "I love "
    else:
        feel+= "I hate "

print(f"{feel}it")