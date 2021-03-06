Method 1: O(N) The idea is to run a loop from 1 to n and for each i, 1 <= i <= n, find i2 to sum.
# Python3 Program to find sum of square of first n natural numbers 
  
  
# Return the sum of square of first n natural numbers 
def squaresum(n) : 
  
    # Iterate i from 1 and n finding square of i and add to sum. 
    sm = 0
    for i in range(1, n+1) : 
        sm = sm + (i * i) 
      
    return sm 
  
# Driven Program 
n = 4
print(squaresum(n)) 

OUTPUT: 30
------------------------------

def squaresum(n) : 
    return (n * (n + 1) * (2 * n + 1)) // 6
-------------------------------

def squaresum(n): 
    return (n * (n + 1) / 2) * (2 * n + 1) / 3
