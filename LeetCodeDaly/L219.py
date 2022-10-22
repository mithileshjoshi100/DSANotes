def solve(nums,k):
    n = len(nums)
    i = 0
    prev = []
    st = set()
    while i<=k:
        if nums[i] in st:
            return True
        st.add(nums[i])
        i += 1
    print(prev)
    while i<n:
        st.remove(nums[i-k-1])
        if nums[i] in st:
            return True
        st.add(nums[i])
        i += 1
        print(st)
    return False



nums = [1,2,3,1]
k = 3
print(solve(nums,k))