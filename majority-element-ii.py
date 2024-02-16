class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_map = Counter(nums)
        ans = set()

        for x in nums:
            if hash_map[x] > len(nums)//3:
                ans.append(x)

        return ans