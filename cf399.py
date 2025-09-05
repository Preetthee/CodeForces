addition = str(input())

numbers = addition.split("+")
numbers.sort()
numbers = "+".join(numbers)

print(numbers)