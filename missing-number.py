class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_map = collections.Counter(nums)

        for i in range(len(nums)+1):
            if not hash_map[i]:
                return i
        

        