def palindrome(string,n,x):
    if n>=x//2:
        print("PALINDROME")
        return
    if string[n]!=string[x-n-1]:
        print("NOT PALINDROME")
        return
    palindrome(string,n+1,x)
palindrome("12222123",0,3)