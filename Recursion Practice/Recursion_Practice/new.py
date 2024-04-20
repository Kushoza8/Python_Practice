class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        new_arr=[]
        my_dict={}
        for i in range(len(nums2)):
            while len(new_arr)!=0 and nums2[new_arr[-1]]<nums2[i]:
                my_dict[nums2[new_arr[-1]]]=nums2[i]
                new_arr.pop()
            new_arr.append(i)
        for i in range(len(new_arr)):
            my_dict[nums2[new_arr[-1]]]=-1
            new_arr.pop()
        for i in range(len(nums1)):
            nums1[i]=my_dict[nums1[i]]
        return nums1
sol=Solution()
print(sol.nextGreaterElement([4,1,2],[1,3,4,2]))