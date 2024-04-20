#recursion to count number of digits in a number
def count_no_digits(n,idx,count):
    string_no=str(n)
    if idx==len(string_no):
        print(count)
        return
    count_no_digits(n,idx+1,count+1)
num=int(input("enter a number: "))
if num<0:
    print("enter a positive number")
else:
    count_no_digits(num,0,0)
    