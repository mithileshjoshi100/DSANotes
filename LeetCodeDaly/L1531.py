'''
Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".
Notice that in this problem, we are not adding '1' after single characters.
Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.
Find the minimum length of the run-length encoded version of s after deleting at most k characters.
'''

def solve(currentIndex, letterLength, k, prevChar, string, memo):
    '''
    This Function return the optimal length after conpretion for string[currentIndex : ]
    '''
    if ( (currentIndex,letterLength,k,prevChar) in memo ): return memo[(currentIndex,letterLength,k,prevChar)]
    if k < 0: return float('inf')
    if currentIndex >= len(string): return 0

    # we have two choise we can delet the element or keep the element
    # delet the element
    delet = solve(currentIndex+1, letterLength, k-1, prevChar, string,memo)
    # keep the element
    keep = 0
    if prevChar == string[currentIndex]:
        if letterLength == 1 or letterLength == 9 or letterLength == 99:
            keep += 1
        keep += solve(currentIndex+1,letterLength+1,k,prevChar,string,memo)
    else:
        keep = 1 + solve(currentIndex+1,1,k,string[currentIndex],string,memo)
    
    memo[(currentIndex,letterLength,k,prevChar)] =  min(keep,delet )
    return memo[(currentIndex,letterLength,k,prevChar)]

def getLengthOfOptimalCompression(s:str, k:int)->int:
    '''
    >>> getLengthOfOptimalCompression("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",0)
    4
    >>> getLengthOfOptimalCompression("aaabcccd",2)
    4
    >>> getLengthOfOptimalCompression("aabbaa",2)
    2
    '''
    memo = {}
    return solve(0,0,k,'.',s,memo)

if __name__ == '__main__':
    import doctest
    doctest.testmod()