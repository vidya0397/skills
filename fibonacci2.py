# Python Program to find position of n\'th multiple of a mumber k in Fibonacci Series 
  
def findPosition(k, n): 
    f1 = 0
    f2 = 1
    i =2;  
    while i!=0: 
        f3 = f1 + f2; 
        f1 = f2; 
        f2 = f3; 
  
        if f2%k == 0: 
            return n*i 
  
        i+=1
          
    return 
  
  
# Multiple no. 
n = 5; 
# Number of whose multiple we are finding 
k = 4; 
  
print("Position of n\'th multiple of k in"
                "Fibonacci Seires is", findPosition(k,n)); 

OUTPUT: 
Position of n'th multiple of k inFibonacci Seires is 30

----------------------------------------
# python program to check if x is a perfect square 
import math 
  
# A utility function that returns true if x is perfect square 
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  
# Returns true if n is a Fibinacci Number, else false 
def isFibonacci(n): 
  
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
    # is a perferct square 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
     
# A utility function to test above functions 
for i in range(1,11): 
     if (isFibonacci(i) == True): 
         print i,"is a Fibonacci Number"
     else: 
         print i,"is a not Fibonacci Number "

 OUTPUT:
1 is a Fibonacci Number
2 is a Fibonacci Number
3 is a Fibonacci Number
4 is a not Fibonacci Number 
5 is a Fibonacci Number
6 is a not Fibonacci Number 
7 is a not Fibonacci Number 
8 is a Fibonacci Number
9 is a not Fibonacci Number 
10 is a not Fibonacci Number             
