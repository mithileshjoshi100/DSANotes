'''
 return the all permutaion of array
 >>> permute([1, 2, 3])
 [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''
def permute(arr,a,ans):
    if a == len(arr):
        ans.append(arr[::])
        return
    for i in range(a,len(arr)):
        arr[a],arr[i] = arr[i],arr[a]
        permute(arr,a+1,ans)
        arr[a],arr[i] = arr[i],arr[a]
ans = []
permute(['A','B','C','D'],0,ans)
print(ans)