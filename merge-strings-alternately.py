# time complexity = O(n)
# space complexity = O(1)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""
        current = 0 
        
        # iterating through both words and appending them
        while len(word1) > current and len(word2) > current:
            merged_string += word1[current]
            merged_string += word2[current]

            current += 1

        # checking if there is some character left in both word
        if current < len(word1):
            merged_string += word1[current:]
        elif current < len(word2):
            merged_string += word2[current:]

        return merged_string
        