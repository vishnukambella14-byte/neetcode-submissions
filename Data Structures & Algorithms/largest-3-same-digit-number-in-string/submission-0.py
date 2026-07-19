class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=""
        for i in range(len(num)-2):
            sub=num[i:i+3]
            if(sub[0]==sub[1]==sub[2]):
                ans=max(ans,sub)
        return ans
            
        