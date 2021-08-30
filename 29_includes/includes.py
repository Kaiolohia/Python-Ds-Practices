def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    if type(collection) == type(""):
        if collection.find(sought,start) != -1:
            return True
        return False
    if type(collection) == type([]) or type(collection) == type((1,2)):
        if start:
            collection = collection[start:]
        if sought in collection:
            return True
        return False
    if type(collection) == type({1,2}):
        if sought in collection:
            return True
        return False
    if type(collection) == type({"key": "Value"}):
        collection = collection.values()
        if sought in collection:
            return True
        return False
