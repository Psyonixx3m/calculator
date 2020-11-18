calculation = input("Enter a operation: ")

if (
    calculation == "+"
    or calculation == "-"
    or calculation == "*"
    or calculation == "/"
):
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    if calculation == "+":
        result = float(num1) + float(num2)
    elif calculation == "-":
        result = float(num1) - float(num2)
    elif calculation == "*":
        result = float(num1) * float(num2)
    elif calculation == "/":
        result = float(num1) / float(num2)
    print(result)
else:
    print("N/a")
