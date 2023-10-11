class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        gap = 0
        nums.sort()
        for i in range(len(nums)-1):
            gap = max(gap,nums[i+1] - nums[i])

        return gap 
        
