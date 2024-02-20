class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        l = 0
        while l < len(nums):
            if nums[l] == 0:
                ptr = l+1
                while ptr < len(nums):
                    if nums[ptr] != 0:
                        nums[l], nums[ptr] = nums[ptr], nums[l]
                        break
                    ptr += 1
            l += 1

        return nums 