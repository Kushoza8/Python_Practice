# NON-RECURSIVE METHOD.
# nums=[1,2,3,4,5]
# start=0
# end=len(nums)-1
# while start<=end:
#     nums[start],nums[end]=nums[end],nums[start]
#     start+=1
#     end-=1
# print(nums)

#RECURSIVE METHOD.
def arr_reverse(arr,n):
    if n<0:
        return 
    print(arr[n])
    return arr_reverse(arr,n-1)
arr_reverse([1,2,3,4,5],4)
    