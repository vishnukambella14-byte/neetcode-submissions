class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count=[0]*501
        for num in nums:
            count[num]+=1
        for freq in count:
            if freq%2!=0:
                return False
        return True
        