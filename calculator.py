class Calculator:
  """A simple calculator class."""

  def __init__(self):
    pass

  def calculate(self, expression):
    """Evaluates the given mathematical expression.

    Args:
      expression: A mathematical expression in string format.

    Returns:
      The result of the evaluation.
    """

    # Split the expression into operands and operator.
    operands = []
    operator = None
    for char in expression:
      if char in ["+", "-", "*", "/"]:
        operator = char
      else:
        operands.append(float(char))

    # Calculate the result and return it.
    if operator == "+":
      return operands[0] + operands[1]
    elif operator == "-":
      return operands[0] - operands[1]
    elif operator == "*":
      return operands[0] * operands[1]
    elif operator == "/":
      return operands[0] / operands[1]
    else:
      raise ValueError(f"Invalid operator: {operator}")


def main():
  """Prompts the user for an expression to evaluate and prints the result."""

  calculator = Calculator()

  expression = input("Enter an expression to evaluate: ")

  # Calculate the result and print it to the console.
  result = calculator.calculate(expression)
  print(result)


if __name__ == "__main__":
  main()
