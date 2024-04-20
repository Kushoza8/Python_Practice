def num_print(idx,arr,new_arr):
    if idx==len(arr):
        print(new_arr)
        return
    new_arr.append(arr[idx])
    num_print(idx+1,arr,new_arr)
    new_arr.remove(arr[idx])
    num_print(idx+1,arr,new_arr)
num_print(0,[1,2,3],[])