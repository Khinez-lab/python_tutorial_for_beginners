
product_name = "espresso"
product_price = 3

#on_sale = "{} is only {} dollars"
on_sale = "{1} is only {0} dollars"

print(on_sale.format(product_name, product_price))
