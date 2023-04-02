# iterative or non-recursive evaluation of the factorial
def factorialNonRecursive(n):
   fact = 1 # defining the variable that will store the factorial
   # loop over n times to find n!
   for i in range(1,n+1):
       fact = fact*i # iteratively implementing n! = n(n-1)...1
   return fact

# recursive evaluation of the factorial
def factorialRecursive(n):
   if(n==1):
       return 1 # base case
   else:
       return n*factorialRecursive(n-1) # recursively implementing n! = n(n-1)...1
