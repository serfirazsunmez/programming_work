# calculator

def calculator(num1,num2,operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "/":
        return num1 / num2
    elif operator == "*":
        return num1 * num2
    elif operator == "%":
        return num1 % num2

print(calculator(4,2,"*"))