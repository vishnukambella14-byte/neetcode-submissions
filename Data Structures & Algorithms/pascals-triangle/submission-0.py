class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(numRows):
            if i==0:
                ans.append([1])
            if i==1:
                ans.append([1,1])
            if i>1:
                prev=ans[-1]
                curr=[1]
                for j in range(i-1):
                    curr.append(prev[j]+prev[j+1])
                curr.append(1)
                ans.append(curr)
        return ans
        