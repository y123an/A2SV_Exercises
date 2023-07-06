class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(k):
            sum += nums[i]
        
        l = 0
        r = k -1 
        mx = float(sum/k)
        while r < len(nums)-1:
            sum -= nums[l]
            l += 1
            r += 1
            sum += nums[r]
            mx =max(mx,sum/k)
        
        return mx