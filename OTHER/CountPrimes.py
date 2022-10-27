#L204.py

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
 

def countPrimes(n):
    count = 0
    for i in range(1,n,2):
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            count += 1
    return count

# 0 1 2 3 4 5 6 7 8 9 
# 1 1 1 1 0 1 0 1 0 1 

def count_primes(n):
    arr = [1]*(n)
    arr[0] = 0
    arr[1] = 0
    for i in range(2,n//2):
        if arr[i] == 1:
            for j in range(i+1,n):
                if j%i == 0:
                    arr[j] = 0
    ans = 0
    for x in arr: ans += x
    return ans

a = 121
print(count_primes(a)==countPrimes(a))