class Solution:
    def fib(self, n: int) -> int:
        arr=[0]*(n+1)
        if n==0:
            return 0
        if n==1:
            return 1
        else:
            if arr[n]!=0:
                return arr[n]
        sp1=self.fib(n-1)
        sp2=self.fib(n-2)
        arr[n]=sp1+sp2
        return sp1+sp2
sol=Solution()
print(sol.fib(30))
    
    
