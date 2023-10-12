class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        end = 0
        mpp = {}
        size = 0

        for i,x in enumerate(s):
            mpp[x] = i
        
        for i,x in enumerate(s):
            size += 1
            if mpp[x] > end:
                end = mpp[x]
            if i == end:
                ans.append(size)
                size = 0


        return ans