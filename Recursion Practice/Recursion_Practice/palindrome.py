def palindrome(string,idx,new_str):
    if idx<0:
        if string==new_str:
            print("PALINDROME")
            return
        else:
            print("NOT PALINDROME")
            return
    palindrome(string,idx-1,new_str+string[idx])
palindrome("12122",2,"")
    