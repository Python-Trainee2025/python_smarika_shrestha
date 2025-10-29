#4. create a calculator that takes two numbers and an operator (+, -, *, /) and performs the operation.
# Handle division by zero and invalid input errors.


try:
    num1, num2, op = input('Enter two numbers and an operator (num,num,operator): ').split(',')
    x = int(num1.strip())
    y = int(num2.strip())
    op = op.strip()

    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == '/':
        try:
            result = x / y
        except ZeroDivisionError:
            result = 'undefined'
    else:
        result = 'Invalid operator'

    print(f'{x} {op} {y} = {result}')

except ValueError:
    print("Invalid input format. Please enter in num,num,operator format.")








