n, k = map(int, input().split())



for i in range(1, k+1):
    last_digit = n % 10
    if last_digit > 0:
        n -= 1
    else:
        n /= 10

n = int(n)

print(n)