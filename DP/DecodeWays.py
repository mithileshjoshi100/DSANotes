def solve(s,i):
    if i > len(s):
        return 0
    if i == len(s):
        return 1
    if s[i] == '0':
        return 0
    if s[i] == '1':
        return solve(s,i+1) + solve(s,i+2)
    if s[i] == '2':
        if i+1<len(s) and s[i+1] <= '6':
            return solve(s,i+1) + solve(s,i+2)
        else:
            return solve(s,i+1)
    return solve(s,i+1)
    

def numDecodings(s):
    '''
    >>> numDecodings('12')
    2
    >>> numDecodings('226')
    3
    >>> numDecodings('06')
    0
    '''
    return solve(s,0)
    pass

print(numDecodings(input()))