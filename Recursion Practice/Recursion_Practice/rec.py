#next greater element-I
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        my_dict={}
        new_arr=[0]
        for i in range(1,len(nums2)):
            if nums2[i]>nums2[new_arr[-1]]:
                while len(new_arr)!=0:
                    if nums2[i]>nums2[new_arr[-1]]:
                        my_dict[nums2[new_arr[-1]]]=nums2[i]
                        nums2[new_arr[-1]]=nums2[i]
                        new_arr.pop()
                new_arr.append(i)
            else:
                new_arr.append(i)
        while len(new_arr)!=0:
            my_dict[nums2[new_arr[-1]]]=-1
            nums2[new_arr[-1]]=-1
            new_arr.pop()
        for i in range(len(nums1)):
            nums1[i]=my_dict[nums1[i]]
        return nums1
sol=Solution()
print(sol.nextGreaterElement([4,1,2],[1,3,4,2]))