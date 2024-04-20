class Solution:
    def reverseVowels(self, s: str) -> str:
        god_list=list(s)
        left=0
        right=len(s)-1
        vowel_list=['a','e','i','o','u','A','E','I','O','U']
        while left<=right:
            if god_list[left] in vowel_list and god_list[right] in vowel_list:
                god_list[left],god_list[right]=god_list[right],god_list[left]
                left+=1
                right-=1
            elif god_list[left] in vowel_list and god_list[right] not in vowel_list:
                right-=1
            elif god_list[left] not in vowel_list and god_list[right] in vowel_list:
                left+=1
            else:
                left+=1
                right-=1
        new_string="".join(god_list)
        return new_string
sol=Solution()
print(sol.reverseVowels("yo! Bottoms Up, u.S. Motto, boy!"))