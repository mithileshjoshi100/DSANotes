# Printing all permutation {POWER SET} using bitmask

# using recursion
def rsolve(s,i,word,lst):
    if i == len(s):
        lst.append(word)
        return
    rsolve(s,i+1,word,lst)
    rsolve(s,i+1,word+s[i],lst)
#lst = []
#rsolve('abc',0,'',lst)
#print(lst)

# using bitmask
def power_set(s):
    lst = []
    n = len(s)
    for x in range(1<<n):
        word = ''
        i = 0
        while x:
            if x&1:
                word = s[i] + word
            x = x >> 1
            i += 1
        lst.append(word[::-1])
    return lst

print(power_set('abc'))
#bits(8)