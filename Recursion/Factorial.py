# Recursion is a technique where a function calls itself.
# It's useful for solving problem that can be broken down into smaller ,similar sub- problems. 


def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)



print(factorial(5))
# Example
# print(factorial(5))  # Output: 120    
