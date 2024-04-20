def ClimbStairs(n,arr1):
    if n==0:
        return 1
    if n<1:
        return 0
    else:
        if arr1[n]!=0:
            return arr1[n]
    sp1=ClimbStairs(n-1,arr1)
    sp2=ClimbStairs(n-2,arr1)
    arr1[n]=sp1+sp2
    return sp1+sp2
arr1=[0]*10000
print(ClimbStairs(500,arr1))

