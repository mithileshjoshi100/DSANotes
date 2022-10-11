'''
    consider two big numbers let first and second
    travel throuch array
    if current element is small than first make is as first
    if current element if greter than first but smaler than second then make it as a second
    if current element is greter than both first and second then it is third greter elemnet:
        so we get ans return True
    
    if nothing get after group then return False
'''


def increasingTriplet(nums:list[int]) -> bool:
    ''' 
    >>> increasingTriplet([5,1,6])
    False
    >>> increasingTriplet([2,1,5,0,6])
    True
    >>> increasingTriplet([2,1,5,0])
    False
    '''
    first = secod = float('inf')
    for x in nums:
        if x <= first:
            first = x
        elif x<= secod:
            secod = x
        else:
            return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()