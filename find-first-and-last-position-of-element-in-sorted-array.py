class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = right = -1
        l, r = 0 , len(nums) -1

        while l <= r:
            mid = (l+r)//2 
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                left = mid
                r = mid - 1
        
        l, r = 0 , len(nums) -1
        
        while l <= r:
            mid = (l+r)//2 
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                right = mid
                l = mid + 1

        return [left,right]
    