def factorial(fact,start,end):
    if start>end:
        print(fact)
        return
    else:
        factorial(fact*end,start,end-1)
factorial(1,1,6)
    