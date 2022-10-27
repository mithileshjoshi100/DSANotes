def threeSum(nums):
    n = len(nums)
    ans = []
    for i in range(n):
        x = twoSum(nums,-nums[i])
        if x: 
            temp = sorted([nums[i]]+x)
            if temp not in ans:
                ans.append(temp)
    
    return ans
def twoSum(nums,v):
    d = set()
    for x in nums:
        if v-x in d:
            return [x,v-x]
        d.add(x)
    

nums = [-1,0,1,2,-1,-4]
k = 100
print(threeSum(nums))