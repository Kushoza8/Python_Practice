#count occurence of a character in a string.
def count_no(string,start,end,character,count):
    if start==end:
        print(count)
        return
    if string[start]==character:
        count_no(string,start+1,end,character,count+1)
    elif string[end]==character:
        count_no(string,start,end-1,character,count+1)
    else:
        count_no(string,start+1,end-1,character,count)
string_inp="pythonooorr"
count_no(string_inp,0,len(string_inp)-1,"o",0)