def calculator(a,b,operation):
    if operation == '+': # Q 20 - to check if the operation is addition
        return a+b
    elif operation == '-': # Q 20 - to check if the operation is subtraction
        return a-b
    elif operation == '*': # Q 20 - to check if the operation is multiplication
        return a*b
    elif b != 0 and operation == '/': # Q 20 - to check if the operation is division
        return a/b
    else:
        return "Error: Invalid operation or division by zero."
a = int(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /): ")
b = int(input("Enter the second number: "))
result = calculator(a, b, operation) # Q 20 - to call the calculator function with arguments a, b and operation and store the result in a variable
print(result) # Q 20 - to call the calculator function with arguments a, b and operation and print the result    
