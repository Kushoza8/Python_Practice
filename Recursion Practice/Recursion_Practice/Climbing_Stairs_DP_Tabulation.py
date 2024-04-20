class Solution:
    def climbStairs(self, n: int) -> int:
        arr=[0]*10000
        arr[1]=1
        arr[0]=1
        for i in range(2,n+1):
            sp1=arr[i-1]
            sp2=arr[i-2]
            arr[i]=sp1+sp2
        return arr[n]
sol=Solution()
print(sol.climbStairs(45))
        