class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        my_dict = {}
        for num in nums:
            if num in my_dict:
                return num
            else:
                my_dict[num] = 1
sol = Solution()
print(sol.findDuplicate([2, 2, 2, 2, 2]))
