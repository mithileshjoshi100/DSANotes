''' 
triangle : sum of two smaller side must me greter than larges side
sort the nums in reverse order : O(nlog(n))
check triplets  O(n)
return sum if found or else return 0
TC : O(nlog(n))
SC : O(1)
'''

def largestPerimeter(nums:list[int]) -> int:
    '''
    >>> largestPerimeter([2,1,2])
    5
    >>> largestPerimeter([1,2,1])
    0
    '''
    nums.sort(reverse=True)
    for i in range(len(nums)-2):
        if nums[i] < nums[i+1] + nums[i+2]:
            return nums[i] + nums[i+1] + nums[i+2]

    return 0


    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()


