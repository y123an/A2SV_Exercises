class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l, r  = 0, n
        ans = []
        while r < len(nums):
            ans.append(nums[l])
            ans.append(nums[r])
            l += 1
            r += 1
        
        return ans