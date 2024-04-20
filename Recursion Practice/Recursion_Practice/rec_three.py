def print_arr_str(idx,arr,string):
    if idx==len(arr):
        print(string)
        return
    print_arr_str(idx+1,arr,string+str(arr[idx]))
print_arr_str(0,[1,2,3,4,5,6,7,8],"")