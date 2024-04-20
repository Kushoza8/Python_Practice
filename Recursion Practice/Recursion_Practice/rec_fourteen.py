def print_no(i,n):
    if i>n:
        return
    print(i)
    print_no(i+1,n)
print_no(1,8)