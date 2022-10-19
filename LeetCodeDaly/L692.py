'''
Remark needs better solution by TC
try using heap

'''

def topKFrequent(words:list[int],k:int):
    '''
    TC: nlon(n) + n*k => O(n*n)
    SC: n => O(n)
    >>> topKFrequent(["i","love","leetcode","i","love","coding"],2)
    ['i', 'love']
    >>> topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4)
    ['the', 'is', 'sunny', 'day']
    '''
    ans = []
    words.sort()
    frmap = {}
    for word in words:
        frmap[word] = frmap.get(word,0)+1
    for _ in range(k):
        mx = 0
        word = ''
        for key in frmap:
            if frmap[key]>mx:
                mx = frmap[key]
                word = key
        ans.append(word)
        frmap[word] = 0
    return ans

if __name__ == '__main__':
    import doctest
    doctest.testmod()