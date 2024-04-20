def reverse_num(nums,n,x):
    if n>=x//2:
        print(nums)
        return
    else:
        nums[n],nums[x-n-1]=nums[x-n-1],nums[n]
        reverse_num(nums,n+1,x)
reverse_num([1,2,3,4],0,4)