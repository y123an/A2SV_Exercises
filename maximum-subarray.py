class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        ac = 0

        for n in nums:
            if ac < 0:
                ac = 0
            ac += n
            maxsub = max(maxsub , ac)
        
        return maxsub
