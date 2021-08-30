def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_return = []
    for ltr in phrase:
        if ltr.lower() == to_swap:
            if ltr.islower():
                to_return.append(ltr.upper())
            else:
                to_return.append(ltr.lower())
        else:
            to_return.append(ltr)
    return to_return