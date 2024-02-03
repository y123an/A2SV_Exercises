# time complexity = O(n)
# space complexity = O(1)

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        final_value = 0

        for x in operations:
            if x == "++X" or x == "X++":
                final_value += 1
            else:
                final_value -= 1
        
        return final_value

        