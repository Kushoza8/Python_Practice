def sum_nums(n,sum):
    if n==0:
        print(sum)
        return 
    sum_nums(n-1,sum+n)
sum_nums(6,0)
#THIS IS THE PARAMTERISED FUNCTION.