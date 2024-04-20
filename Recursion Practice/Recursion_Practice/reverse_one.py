def arr_reverse(arr,start,end):
    if start>=end:
        print(arr)
        return
    arr[start],arr[end]=arr[end],arr[start]
    arr_reverse(arr,start+1,end-1)
arr_reverse([1,2,3,4,5,6],0,5)
      