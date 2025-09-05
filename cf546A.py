first_banana, current_money, banana_count = map(int, input().split())

total_price = 0

for i in range(1, banana_count + 1):
    total_price += first_banana * i

money_needed = total_price - current_money

if money_needed < 0:
    money_needed = 0
    
print(money_needed)