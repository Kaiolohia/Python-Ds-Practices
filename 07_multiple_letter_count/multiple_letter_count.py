def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    initSet = set(phrase.lower())
    initDict = {char:0 for char in initSet}
    for letter in phrase:
        initDict[letter.lower()] += 1
    return initDict
    