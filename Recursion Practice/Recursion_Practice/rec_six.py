def sum_num(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return n+sum_num(n-1)
print(sum_num(5))