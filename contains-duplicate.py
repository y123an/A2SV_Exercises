class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # a hashmap for tracking the numbers occurance
        hashmap = collections.Counter()
        
        # iterating throuth the elements and counting the occurance
        for num in nums:
            if hashmap[num]:
                return True
            hashmap[num] += 1
        
        return False
        