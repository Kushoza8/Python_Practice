def print_no(i,n):
    if i>n:
        return
    print_no(i+1,n)
    print(i)
print_no(1,5)