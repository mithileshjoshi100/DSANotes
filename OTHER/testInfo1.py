def findRange(n,A,k):
    A.sort(reverse=True)
    ans = 0
    for i in range(k):
        ans = ans + A.pop() - 1
    return ans 

n = 4
A = [1,1,4,2]
k = 1
print(findRange(n,A,k))