class Solution:
    def getSum(self, a: int, b: int) -> int:
        count=0
        if a>0 and b>0:
            while b>0:
                b=b-1
                count+=1
            while a>0:
                a=a-1
                count+=1
            return count
        else:
            return sum([a,b])
sol=Solution()
print(sol.getSum(-1,1))
    
    
