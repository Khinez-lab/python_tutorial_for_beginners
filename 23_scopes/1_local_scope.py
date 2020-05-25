def calculate_amount(prices):
    amount = 0
	
    for price in prices:
        amount += price
	
    return amount

result = calculate_amount([50, 100, 150])

print(result)