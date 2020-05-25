def calculate_amount(prices):
    global extra_price

    extra_price = 20
    amount = 0

    for price in prices:
        amount += price

    amount += extra_price

    return amount

extra_price = 10
amount = calculate_amount([50, 100, 150])

print(extra_price)
print(amount)