class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        res=0
        for num in nums:
            if num==1:
                count+=1
                
            
            if num==0:
                res=max(count,res)
                count=0
            
        return max(res,count)
        