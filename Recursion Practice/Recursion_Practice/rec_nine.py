def palindrome_str(string,idx,new_palindrome_str):
    if idx<0:
        if string==new_palindrome_str:
            print(new_palindrome_str)
            print("THIS IS A PALINDROME")
        else:
            print("THIS IS NOT A PALINDROME")
        return
    palindrome_str(string,idx-1,new_palindrome_str+string[idx])
string_inp=input("enter string: ")
palindrome_str(string_inp,len(string_inp)-1,"")
#CHECK EFFICIENT APPROACH ON CHATGPT.