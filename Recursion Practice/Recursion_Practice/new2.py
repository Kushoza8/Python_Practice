class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        i=len(nums)-2
        if len(nums) < 2:
            return nums
        if nums[-1] > nums[-2]:
            nums[-1], nums[-2] = nums[-2], nums[-1]
            return nums
        else:
            while i>0:
                if nums[i]>nums[i-1]:
                    nums[i-1],nums[-1]=nums[-1],nums[i-1]
                    # Reverse the sublist of nums starting from index i
                    left, right = i, len(nums) - 1
                    while left < right:
                        nums[left], nums[right] = nums[right], nums[left]
                        left += 1
                        right -= 1
                    return nums
                    break
                elif nums[i-1]>nums[i] and i==1:
                    nums.reverse()
                    return nums
                i-=1
sol=Solution()
print(sol.nextPermutation([2,3,1]))
        
