class Solution:
    def reverseWords(self, s: str) -> str:
        list_of_words=s.split(" ")
        for i in range(len(list_of_words)):
            left=0
            right=len(list_of_words[i])-1
            new_list=list(list_of_words[i])
            while left<=right:
                new_list[left],new_list[right]=new_list[right],new_list[left]
                left+=1
                right-=1
            list_of_words[i]="".join(new_list)      
        return " ".join(list_of_words)     
sol=Solution()
print(sol.reverseWords("Let's take LeetCode contest"))