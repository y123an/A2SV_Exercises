class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        longest = 0
        l = 0
        count = 0
        for r in range(N):
            if nums[r] == 0:
                count += 1
            
            while count > 1:
                if nums[l] == 0:
                    count -= 1
                l += 1
            longest = max(longest, r-l)

        return longest