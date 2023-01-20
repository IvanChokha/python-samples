class IntervalsError(Exception):
    """Error of invervals."""


def concatenate_intervals(
    intervals: list[list[int, int]]
) -> list[list[int, int]]:
    """
    From a given list of intervals, get the minimum list
    of non-overlapping intervals.

    :param intervals: Intervals from one integer to another.
        For instance: `[[1, 9], [6, 10], [12, 17], [13, 15]]`.
    :type intervals: list[list[int, int]]
    :raises IntervalsError: Invalid list of intervals or invalid
        single interval.
    :return: List of non-overlapping intervals.  For instance:
        `[[1, 10], [12, 17]]`
    :rtype: list[list[int, int]]
    """
    if not (isinstance(intervals, list) and len(intervals) > 0):
        raise IntervalsError("Invalid intervals")

    sorted_intervals = sorted(intervals, key=lambda item: item[0])
    result = [sorted_intervals[0]]
    for i in sorted_intervals:
        if not (
            isinstance(i, list) and len(i) == 2 and isinstance(i[0], int),
            isinstance(i[1], int),
        ):
            raise IntervalsError(f"Invalid interval: {i}")

        last = result[-1]
        if i[0] <= last[1] + 1:
            if last[1] < i[1]:
                last[1] = i[1]
        else:
            result.append(i)

    return result
