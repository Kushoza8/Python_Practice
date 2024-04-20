class Solution:
    def partition(self, s: str) -> list[str]:
        res=[]
        DigitstoChar={
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        def backTrack(i, Currstr):
            if len(s) == len(Currstr):
                res.append(Currstr)
                return
            for c in DigitstoChar[s[i]]:
                backTrack(i + 1, Currstr + c)
        if s:
            backTrack(0, "")
        return res

sol = Solution()
print(sol.partition("23"))
