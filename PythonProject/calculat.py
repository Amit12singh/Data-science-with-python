def is_valid_expression(expr):
    allowed_chars = "0123456789+-*/(). "
    return all(char in allowed_chars for char in expr)


print("Welcome to the Smart Calculator!")
print("You can enter full expressions like: 5 + 3 * 2 - 1 / 4")

while True:
    expr = input("\nEnter expression (or type 'exit' to quit): ").strip()

    if expr.lower() == "exit":
        print("Goodbye!")
        break

    if not is_valid_expression(expr):
        print("Invalid characters detected. Please enter numbers and + - * / ( ) only.")
        continue

    try:
        result = eval(expr)
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print("Invalid expression! Please check your syntax.")
