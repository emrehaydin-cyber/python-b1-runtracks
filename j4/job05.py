def any_computation(num1,operator,num2):
    if operator == "*":
        return num1 * num2
    elif operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        print("impossible d'effectuer l'operation")
any_computation(5,"+",5)
print(any_computation(5,".",5))