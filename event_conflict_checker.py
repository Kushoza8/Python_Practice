class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        if event2[0]<=event1[1] and event1[0]<=event2[1]:
            return True
        else:
            return False
sol=Solution()
print(sol.haveConflict(["14:13","22:08"],["02:40","08:08"]))    
        
        