word_correct = str(input())
word_reversed = str(input())
reversed = word_correct[::-1]
if word_reversed == reversed:
    print("YES")
else:
    print("NO")