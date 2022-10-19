def countSmaller(nums):
    '''
    >>> countSmaller([5, 2, 6, 1])
    [2, 1, 1, 0]
    >>> countSmaller([-1, -1])
    [0, 0]
    '''
    n = len(nums)
    ans = []
    for i in range(n):
        count = 0
        for j in range(i+1,n):
            if nums[i] > nums[j]:
                count += 1
        ans.append(count)
    return ans

if __name__ == '__main__':
    import doctest
    doctest.testmod()