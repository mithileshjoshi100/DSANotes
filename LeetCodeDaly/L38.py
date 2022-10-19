def code(s):
    '''
    >>> code('AABBB')
    2A3B
    >>> code('ABBBBC')
    1A4B1C
    '''
    ans = ''
    i = 1
    char,count = s[0],1
    while i < len(s):
        #print(i,char)
        if s[i] == char:
            count += 1
        else:
            ans += str(count)+str(char)
            char = s[i]
            count = 1
        i += 1
    ans += str(count)+str(char)
    return ans
#print(code('ZAABBBBCCCDX'))

def solve(n):
    if n == 1:
        return '1'
    n1 = solve(n-1)
    return code(n1)
print(solve(4))
