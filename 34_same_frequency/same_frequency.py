def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    freq1 = {}
    freq2 = {}
    num1 = list(str(num1))
    num2 = list(str(num2))
    if len(num1) != len(num2):
        return False
    for num in range(len(num1)):
        if num1[num] not in freq1:
            freq1[num1[num]] = 1
        else:
            freq1[num1[num]] += 1
    for num in range(len(num2)):
        if num2[num] not in freq2:
            freq2[num2[num]] = 1
        else:
            freq2[num2[num]] += 1
    for num in freq1:
        if freq1[num] != freq2[num]:
            return False
    return True
        