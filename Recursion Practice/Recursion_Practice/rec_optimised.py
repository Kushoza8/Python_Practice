#next greater element
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        my_dict={}
        stack=[]
        for num in nums2:
            while stack and stack[-1]<num:
                my_dict[stack.pop()]=num
            stack.append(num)
        for num in stack:
            my_dict[num]=-1
        result = [my_dict[num] for num in nums1]
        return result
sol = Solution()
print(sol.nextGreaterElement([2,4],[1,2,3,4]))