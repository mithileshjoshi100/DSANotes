from collections import deque

def solve(nums,k):
    ans = []
    n = len(nums)
    i = 0 
    cmax = float('-inf')
    mx2 = float('-inf')
    q = deque()
    while i < k:
        q.append(nums[i])
        i += 1
    print(q)
    while i < n:
        temp = q.popleft()
        q.append(nums[i])
        print(q)
        i += 1
    return ans
    pass

print(float('-inf'))
nums = [1,3,1,2,0,5]
k = 3

print(solve(nums,k))