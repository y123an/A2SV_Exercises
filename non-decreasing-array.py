class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        dummy = nums.copy()
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                nums[i] = nums[i - 1]
                dummy[i - 1] = dummy[i]
                break
        return nums == sorted(nums) or dummy == sorted(dummy)