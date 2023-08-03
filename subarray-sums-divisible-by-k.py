class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = [0]*k

        sum = 0

        for x in nums:
            sum += x%k
            counts[sum%k] += 1
        
        result = counts[0]

        for c in counts:
            result += (c*(c-1))//2
        
        return result