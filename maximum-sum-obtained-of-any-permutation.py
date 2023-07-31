class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 1_000_000_007
        n = len(nums)

        prefix = [0] * n

        for re in requests:
            prefix[re[0]] += 1
            if re[1] + 1 < n:
                prefix[re[1]+1] -= 1
        ac = 0

        for i in range(len(prefix)):
            prefix[i] += ac
            ac = prefix[i]
        
        nums.sort()
        prefix.sort()

        sum = 0

        for i in range(n):
            sum += prefix[i] * nums[i]
        
        return sum % MOD

