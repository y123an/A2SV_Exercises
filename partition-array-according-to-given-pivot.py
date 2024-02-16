class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than = []
        greater_than = []
        middle = []

        for x in nums:
            if x > pivot:
                greater_than.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                less_than.append(x)

        return less_than + middle + greater_than
        