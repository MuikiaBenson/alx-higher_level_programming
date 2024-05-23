def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    mid = len(list_of_integers) // 2

    # Check if mid element is peak
    if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
       (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
        return list_of_integers[mid]

    # If right neighbor is greater, search right half
    if mid < len(list_of_integers) - 1 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid + 1:])
    
    # Otherwise, search left half
    return find_peak(list_of_integers[:mid])
