def calculator():
    
    num1= float(input("Enter the first number:"))
    num2= float(input("Enter the second number:"))
    operator= input("Enter the operator (+, -, *, /)")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
       
        if num2 !=0:
            result= num1 / num2
        else:
            print("Error Cannot divide by zero.")
            return
    else:
        print("Invalid operator. Please enter +, -, *, or /.")
        return

   
    print(f"Result: {num1}{operator}{num2} = {result}")

calculator()

