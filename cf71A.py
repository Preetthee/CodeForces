n = int(input())
for _ in range(n):
    word = input().strip()
    if len(word) > 10:
        abbreviated = word[0] + str(len(word) - 2) + word[-1]
        print(abbreviated)
    else:
        print(word)