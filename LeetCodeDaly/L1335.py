'''
1335. Minimum Difficulty of a Job Schedule
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).
You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.
You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].
Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.
'''
# this funtion will return optimal solution from i to end
def solve(i:int, d:int, cmax:int, jobDifficulty:list[int],memo)->int:
    if ((i,d,cmax) in memo): return memo[(i,d,cmax)]
    if i == len(jobDifficulty):
        if d == 0: return 0
        else: return float('inf')
    if d == 0: return float('inf')
    # no partation
    cmax = max(cmax,jobDifficulty[i])
    a1 = solve(i+1,d,cmax,jobDifficulty,memo)
    # partation
    a2 = cmax + solve(i+1,d-1,0, jobDifficulty,memo)
    memo[(i,d,cmax)] =  min(a1,a2)
    return memo[(i,d,cmax)]
    


def minDifficulty(jobDifficulty, days):
    '''
    >>> minDifficulty([11,111,22,222,33,333,44,444],6)
    843
    >>> minDifficulty([6,5,4,3,2,1],2)
    7
    >>> minDifficulty([9,9,9],4)
    -1
    >>> minDifficulty([1,1,1],3)
    3
    '''
    memo = {}
    ans = solve(0,days,0,jobDifficulty,memo)
    return -1 if ans == float('inf') else ans

if __name__ == '__main__':
    import doctest 
    doctest.testmod()