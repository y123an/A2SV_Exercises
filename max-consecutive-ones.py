class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum_count = 0
        current_count = 0

        # keeping truck of the current count of the 1 and if there is 0 update the max
        for num in nums:
            if num == 0:
                maximum_count = max(maximum_count,current_count)
                current_count = 0
            else:
                current_count += 1
                
        # if the loop finish without seeing 0
        maximum_count = max(current_count, maximum_count)

        return maximum_count
