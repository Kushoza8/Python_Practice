def palindrome(string,i,n):
    if i>=n//2:
        return True
    if string[i]!=string[n-i-1]:
        return False
    return palindrome(string,i+1,n)
print(palindrome("radar",0,5))        
