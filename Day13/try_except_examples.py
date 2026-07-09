# Example 1: Handling division by zero

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")

except ZeroDivisionError:
    print("You cannot divide by zero!")

except ValueError:
    print("Please enter a valid number.")