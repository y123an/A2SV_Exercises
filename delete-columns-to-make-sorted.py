class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0

        for idx_col in range(len(strs[0])):
            for idx_row in range(len(strs)-1):
                if strs[idx_row][idx_col] > strs[idx_row + 1][idx_col]:
                    count += 1
                    break
        
        return count