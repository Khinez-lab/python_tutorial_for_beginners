number_1 = input("Number1: ")
number_2 = input("Number2: ")
operation = input("Operation (+ - * /): ")

result = None

number_1 = int(number_1)
number_2 = int(number_2)

if operation == "+":
    result = number_1 + number_2
elif operation == "-":
    result = number_1 - number_2
elif operation == "*":
    result = number_1 * number_2
elif operation == "/":
    result = number_1 / number_2

print(result)
