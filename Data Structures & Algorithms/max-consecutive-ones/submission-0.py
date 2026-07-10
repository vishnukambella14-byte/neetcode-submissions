class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        res=[]
        for num in nums:
            if num==1:
                count+=1
                res.append(count)
            
            elif num==0:
                res.append(count)
                count=0
            
        return int(max(res))
        