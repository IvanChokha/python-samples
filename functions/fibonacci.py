def fibonacci(n: int) -> int:
    """Get n-th Fibonacci number.

    :param n: index of Fibonacci number.
    :type n: int
    :raises ValueError: Invalid given number.
    :return: Fibonacci number
    :rtype: int
    """
    if n < 1:
        raise ValueError("Invalid given nubmer")
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
