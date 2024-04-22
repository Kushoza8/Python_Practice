#string use karne se - sign ka problem hora isliye use nhi kiya
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def permutations(nums1, perm, start, end, result):
            if start == end:
                result.append(perm) 
                return
            for num in nums1:
                new_nums = nums1.copy()
                new_nums.remove(num)
                permutations(new_nums, perm + [num], start + 1, end, result)
        result = []
        permutations(nums, [], 0, len(nums), result) 
        return result

sol = Solution()
print(sol.permute([0, -1, 1]))
