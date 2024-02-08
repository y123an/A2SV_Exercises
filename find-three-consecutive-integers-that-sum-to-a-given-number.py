class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num == 0:
            return [-1,0,1]
        if num % 3:
            return []

        n = num // 3 + 1

        return [n-2,n-1,n]
        