def add(num1, num2):
  """Adds two numbers together."""
  return num1 + num2

def subtract(num1, num2):
  """Subtracts two numbers."""
  return num1 - num2

def multiply(num1, num2):
  """Multiplies two numbers."""
  return num1 * num2

def divide(num1, num2):
  """Divides two numbers."""
  if num2 == 0:
    print("Error: Cannot divide by zero.")
    return None
  else:
    return num1 / num2

while True:
  print("Select an operation to perform:")
  print("1. ADD")
  print("2. SUBTRACT")
  print("3. MULTIPLY")
  print("4. DIVIDE")
  print("5. QUIT")

  choice = input("Enter your choice (1/2/3/4/5): ")

  if choice == '5':
    break

  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
      result = add(num1, num2)
      print(num1, "+", num2, "=", result)
    elif choice == '2':
      result = subtract(num1, num2)
      print(num1, "-", num2, "=", result)
    elif choice == '3':
      result = multiply(num1, num2)
      print(num1, "*", num2, "=", result)
    elif choice == '4':
      result = divide(num1, num2)
      if result is not None:
        print(num1, "/", num2, "=", result)
    else:
      print("Invalid input. Please enter a valid choice.")
  except ValueError:
    print("Error: Invalid input. Please enter numbers only.")

print("Calculator closed.")
