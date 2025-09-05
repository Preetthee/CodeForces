statement_number = int(input())
x = 0
for i in range(statement_number):
    statement = str(input())
    if "++" in statement:
        x += 1
    else:
        x -= 1
print(x)