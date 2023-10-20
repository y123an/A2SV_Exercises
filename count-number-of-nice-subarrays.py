class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

        preHash = collections.Counter()
        preHash[0] += 1
        ac = 0 
        count = 0
        for n in nums:
            ac += n
            count += preHash[ac - k]
            preHash[ac] += 1
        
        return count