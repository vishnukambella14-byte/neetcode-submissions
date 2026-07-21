class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        majorityElement = -1

        for num in nums:
            if counter == 0:
                majorityElement = num
                counter += 1
            else:
                if majorityElement == num:
                    counter += 1
                else:
                    counter -= 1
        
        return majorityElement
        