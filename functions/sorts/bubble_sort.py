def bubble_sort(ints: list[int]) -> list[int]:
    """Sort the given list of integers using the bubble method.

    The optimized version of the algorithm is used:
    https://en.wikipedia.org/wiki/Bubble_sort#Optimizing_bubble_sort

    :param ints: The list of integers to sort.
    :type ints: list[int]
    :return: The new sorted list of integers.
    :rtype: list[int]
    """
    length = len(ints)
    result = ints[:]

    for i in range(length - 1):
        is_swapped = False
        for j in range(i + 1, length):
            if result[i] > result[j]:
                result[j], result[i] = result[i], result[j]
                is_swapped = True

        # If there are no replacements in one of the iterations,
        # then the list is already sorted
        if not is_swapped:
            return result

    return result
