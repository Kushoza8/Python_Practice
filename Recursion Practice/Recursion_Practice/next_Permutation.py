class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        i=len(nums)-1
        while i>0 and nums[i]<=nums[i-1]: #jab nums[i-1]<nums[i] mila tab uss i ko store kar lege.
            i-=1
        if i>0: #ek aur while loop se backtrack comparision karna.
            j=len(nums)-1
            while nums[j]<=nums[i-1]: #ulta greater sign se decrement hote jata try example [7,8,0,4,3,2,1].
                j-=1
            nums[i-1],nums[j]=nums[j],nums[i-1]
        nums[i:]=nums[i:][::-1]
        return nums
sol=Solution()
print(sol.nextPermutation([3,2,1]))