#functional recursion
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(3))
#paramtersied recursion
# def factorial(n,fact):
#     if n==0:
#         print(fact)
#         return 
#     return factorial(n-1,fact*n)
# factorial(5,1)
