class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hash_map = collections.Counter()
       
        for i ,num in enumerate(nums):
            hash_map[num] = i
       
        for operation in operations:
            hash_map[operation[1]] = hash_map[operation[0]] 
            hash_map[operation[0]] = -1
       
        ans = [0] * len(nums)
       
        for x in hash_map:
            if hash_map[x] >= 0:
                ans[hash_map[x]] = x
       
        return ans
       