def ngr(arr:list[int])->list[int]:
    '''
    >>> ngr([2,1,5,0,4,6])
    [2,2,5,4,5,-1]
    '''
    ans = arr[::]
    i = len(arr)-1
    stack = []
    while i>=0:
        if len(stack) == 0:
            ans[i] = -1
            stack.append(arr[i])
            i -= 1
        elif stack[-1] > arr[i]:
            ans[i] = stack[-1]
            stack.appen(arr[i])
            i -= 1
        elif stack[-1] < arr[i]:
            stack.pop()
    return ans

if __name__ == '__main__':
    import doctest
    doctest.testmod()