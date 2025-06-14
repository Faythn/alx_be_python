def perform_operation(num1, num2, operation):
    """Perform an arithmetic operation on two numbers.

    Args:
        num1 (float): The first operand.
        num2 (float): The second operand.
        operation (str): The operation to perform. Accepted values are
            'add', 'subtract', 'multiply', and 'divide'.

    Returns:
        float or str: Result of the arithmetic operation, or an error message for division by zero.
    """
    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Choose from 'add', 'subtract', 'multiply', or 'divide'.")


