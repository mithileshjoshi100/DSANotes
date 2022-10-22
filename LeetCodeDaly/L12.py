'''
Integer To Roman
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

def intToRoman(n:int)->str:
    '''
    >>> intToRoman(3)
    'III'
    >>> intToRoman(58)
    'LVIII'
    >>> intToRoman(1994)
    'MCMXCIV'
    '''
    nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    char = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    i = 0
    ans = ''
    while n > 0:
        if n >= nums[i]:
            ans += char[i]
            n = n - nums[i]
        else:
            i += 1
    return ans

if __name__ == '__main__':
    import doctest
    doctest.testmod()