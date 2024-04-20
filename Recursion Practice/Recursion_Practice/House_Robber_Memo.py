def House_Rob(nums,idx):
    dp=[0]*1000
    if idx>=len(nums):
        return 0
    else:
        if dp[idx]!=0:
            return dp[idx]
    sp1=nums[idx]+House_Rob(nums,idx+2)
    sp2=House_Rob(nums,idx+1)
    dp[idx]=max(sp1,sp2)
    return max(sp1,sp2)
arr1=[1,2,3,2]
print(House_Rob(arr1,0))