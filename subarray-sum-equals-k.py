class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ac = 0
        count = 0
        preHash = collections.Counter()
        preHash[0] += 1

        for n in nums:
            ac += n
            count += preHash[ac - k]
            preHash[ac] += 1

        return count       
