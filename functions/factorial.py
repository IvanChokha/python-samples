def factorial(n: int) -> int:
    """Get factorial of the number.

    :param n: number to calculate factorial.
    :type n: int
    :raises ValueError: Invalid given number.
    :return: Factorial of the number
    :rtype: int
    """
    if n < 1:
        raise ValueError("Invalid number")
    if n <= 2:
        return n
    return factorial(n - 1) * n
