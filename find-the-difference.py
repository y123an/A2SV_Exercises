# time complexity = O(n)
# space complexity = O(1)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        
        # iterating through both sorted strings and try to find the added one
        for i in range(len(s)):
            if sorted_s[i] != sorted_t[i]:
                return sorted_t[i]
        
        # if the loop is finished it means the added character is at the last of the sorted t
        return sorted_t[-1]
