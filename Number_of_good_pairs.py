class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        number_of_pairs = 0

        # iterating through every element 

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    number_of_pairs += 1
        
        return number_of_pairs
        