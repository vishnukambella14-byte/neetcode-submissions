class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]=freq[num]+1
            else:
                freq[num]=1
        sorted_freq=sorted(freq.items(),key=lambda items:items[1],reverse=True)
        result=[key for key,value in sorted_freq[:k]]
        return result

        