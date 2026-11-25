def count_in_list(items, target):
    """
    Count how many items are equal to the target.

    Args:
        items (list): Values to search.
        target (object): Value to count.

    Returns:
        int: Number of items equal to the target.
    """

    count = 0
    for item in items:
        if item == target:
            count += 1
    return count
