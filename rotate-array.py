class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if(k < 0):
            k += len(nums)
            
        l, r = len(nums)-k,len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        print(nums)
        l, r = 0,len(nums)-k-1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l, r = 0,len(nums)-1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1