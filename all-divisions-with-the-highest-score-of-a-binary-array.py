class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        idx_val = [0] * (len(nums)+1)

        a = 0
        new_nums = []
        
        for i in range(len(nums)-1, -1 ,-1):
            new_nums.append(nums[i] + a)
            a += nums[i]
        new_nums.reverse()
        
        idx_val[0] = new_nums[0]
        idx_val[len(nums)] = len(nums) - sum(nums)

        
        count_0 = 0
        for i in range(len(nums)-1):
            if nums[i] == 0:
                count_0 += 1
            idx_val[i+1] = count_0 + new_nums[i+1]

        
        ans = []
        max_ans = max(idx_val)

        for i in range(len(idx_val)):
            if idx_val[i] == max_ans:
                ans.append(i)


        return ans