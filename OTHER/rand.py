# Program to generate a random number between 0 and 9

# importing the random module
import random

def shuffle_arr(arr):
    n = len(arr)-1
    for i in range(5):
        a,b = random.randint(0,n),random.randint(0,n)
        arr[a],arr[b] = arr[b],arr[a]
    return arr

print(shuffle_arr([1,2,3,4,5,6]))