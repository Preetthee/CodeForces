for _ in range(int(input())) : print((w[0] + str(len(w) - 2) + w[-1]) if (w := input()) is not None and len(w)>10 else w)


# n = int(input())
# for _ in range(n):
#     word = input().strip()
#     if len(word) > 10:
#         abbreviated = word[0] + str(len(word) - 2) + word[-1]
#         print(abbreviated)
#     else:
#         print(word)