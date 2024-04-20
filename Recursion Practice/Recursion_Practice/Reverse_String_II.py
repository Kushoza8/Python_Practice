class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list_string=list(s)
        left=0
        while left<len(s):
            list_string[left:left+k]=list_string[left:left+k][::-1]
            print(left+k)
            left+=2*k
        return "".join(list_string)
sol=Solution()
print(sol.reverseStr("abcdefgh",3))