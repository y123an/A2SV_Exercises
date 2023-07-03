class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            sume = numbers[l] + numbers[r]
            if sume == target:
                return [l+1,r+1]
            elif sume < target:
                l += 1
            else:
                r -= 1 
        