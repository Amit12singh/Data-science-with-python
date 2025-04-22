def add(numbers):
    return sum(numbers)

def sub(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def mul(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    try:
        for num in numbers[1:]:
            if num == 0:
                return "Division by zero is not allowed."
            result /= num
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def get_numbers():
    try:
        nums = input("Enter numbers separated by space: ").split()
        return [float(num) for num in nums]
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        return []

print("Welcome to the Advanced Calculator!")

while True:
    print("\nChoose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number between 1 and 5.")
        continue

    if choice == 5:
        print("Exiting calculator. Goodbye!")
        break

    numbers = get_numbers()
    if len(numbers) < 2:
        print("Please enter at least two numbers.")
        continue

    if choice == 1:
        print("Result:", add(numbers))
    elif choice == 2:
        print("Result:", sub(numbers))
    elif choice == 3:
        print("Result:", mul(numbers))
    elif choice == 4:
        print("Result:", divide(numbers))
    else:
        print("Invalid choice! Please select from 1 to 5.")
