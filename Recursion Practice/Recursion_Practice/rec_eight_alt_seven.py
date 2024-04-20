def count_no_digits(n,count):
    if n==0:
        print(count)
        return
    count_no_digits(n//10,count+1)
count_no_digits(123,0)