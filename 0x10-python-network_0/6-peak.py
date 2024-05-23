#!/usr/bin/python3
"""Finds the peak in an unsorted list of integers"""

#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    return _find_peak(list_of_integers, 0, len(list_of_integers) - 1)


def _find_peak(lint, start, stop):
    """Recursively finds a peak in the list."""
    if start == stop:
        return lint[start]

    mid = (start + stop) // 2

    if mid > 0 and lint[mid] < lint[mid - 1]:
        return _find_peak(lint, start, mid - 1)
    elif mid < len(lint) - 1 and lint[mid] < lint[mid + 1]:
        return _find_peak(lint, mid + 1, stop)
    else:
        return lint[mid]
