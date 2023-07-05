class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        r = 1
        u = nums[0]
        cnt = 0

        while r < len(nums):
            if nums[r] != u:
                u = nums[r]
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r += 1
                cnt +=1
            else:
                r += 1 

        return cnt+1
        
        