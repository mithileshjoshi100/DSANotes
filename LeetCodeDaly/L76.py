from collections import Counter
def solve(s,t):
    s_count,t_count = Counter(),Counter(t)
    l,r = 0,0
    n = len(s)
    anss = []
    while r < n:
        #expand
        s_count[s[r]] += 1
        r += 1
        if t_count != (t_count & s_count):
            continue
        # shrink
        while l < r:
            s_count[s[l]] -= 1
            l += 1
            if t_count == (t_count & s_count):
                continue
            anss.append(s[l-1:r])
            break
    print(anss)
    return min(anss,key=len)
            
    print(s_count,t_count)


s = "ADOBECODEBANC"
t = "ABC"
print(solve(s,t))