def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    initSet = set(nums)
    initDict = {char:0 for char in initSet}
    for num in nums:
        initDict[num] += 1
    keys = list(initDict.keys())
    vals = list(initDict.values())
    return keys[vals.index(max(vals))]