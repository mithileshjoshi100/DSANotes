def maxLength(arr):

    pass


def bits(n):
    ans = 0
    for i in range(1<<n):
        s = ''
        ind = 0
        while i:
            if i&1:
                s += arr[ind]
            ind += 1
            i = i // 2
        if len(s) == len(set(s)):
            ans = max(ans,len(s))
    return ans
        

arr = ["un","iq","ue"]
print(bits(3))



print(maxLength(arr))