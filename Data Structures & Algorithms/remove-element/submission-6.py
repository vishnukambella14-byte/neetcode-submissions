class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write=0
        count=0
        for read in range(len(nums)):
            if nums[read]!=val:
                nums[write]=nums[read]
                write+=1
                count+=1
                
        return count        