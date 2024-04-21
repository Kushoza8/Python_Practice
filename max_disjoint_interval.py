class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> list:
        intervals=sorted(intervals,key=lambda x:x[1])
        count=0
        last_interval=intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0]<last_interval[1]:
                count+=1
            else:
                last_interval=intervals[i]     
        return count 
sol=Solution()
print(sol.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
    
                
                
                
                
        
        