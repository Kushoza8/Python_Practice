class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        nums_new=[]
        nums_new=nums+nums
        stack=[]
        for i in range(len(nums_new)):
            while stack and nums_new[stack[-1]]<nums_new[i]:
                nums_new[stack[-1]]=nums_new[i]
                stack.pop()
            stack.append(i)
        while stack:
            nums_new[stack[-1]]=-1
            stack.pop()
        return nums_new[:len(nums)]
sol=Solution()
print(sol.nextGreaterElements([5,4,3,2,1]))