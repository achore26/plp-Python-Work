def calculate(num1,num2,operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Invalid operation"


print("Enter two numbers of your choice")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print("Enter the operation you would like to perform(+,-,/,*)")
operation = input("Enter operation: ")

result = calculate(float(num1),float(num2),operation)


if result == "Invalid operation":
    print("Invalid operation")
else:   
    print(f'{num1} {operation} {num2} = {result}')
