class Solution:
    def rob(self, nums: list[int]) -> int:  
        n=len(nums)      
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        dp=[0]*(len(nums)+1)
        dp[0]=nums[0]
        dp[1]=nums[1]
        dp[2]=nums[2]+nums[0]
        for i in range(3,n):
            dp[i]=max(dp[i-2],dp[i-3])+nums[i]
        return max(dp[n-1],dp[n-2])
sol=Solution()
print(sol.rob([7,2,9,3,1]))
