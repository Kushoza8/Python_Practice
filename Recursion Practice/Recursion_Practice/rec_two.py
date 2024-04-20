def print_num(n,m):
    if n>m:
        return
    print(n)
    print_num(n+1,m)
    print(n)
print_num(1,5)