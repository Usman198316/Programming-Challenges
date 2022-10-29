def main():
    calculation = ""
    while calculation != "q":
        calculation = str(input("Enter your calculation >> "))
        if calculation == "q":
            break
        num1 = int(calculation[0])
        num2 = int(calculation[2])
        if len(calculation) == 5:
            operator = calculation[4]
        else:
            operator = calculation[4] + calculation[5]

        print(calculator(num1, num2, operator))


def calculator(num1, num2, operator):
    result = 0
    if operator == "+":
        result = num1+num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1*num2
    elif operator == "/":
        result = num1 / num2
    elif operator == "//":
        result = num1 // num2
    elif operator == "%":
        result = num1 % num2
    elif operator == "**":
        result = num1 ** num2

    return result


main()
