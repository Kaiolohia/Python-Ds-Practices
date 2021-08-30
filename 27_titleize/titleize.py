def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    words = phrase.split(' ')
    title = []
    for word in words:
        title.append(word.capitalize() + ' ')
    return "".join(title)
print(titleize('this is awesome'))