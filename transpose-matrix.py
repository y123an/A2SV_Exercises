class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []

        for idx_row in range(len(matrix[0])):
            temp = []
            for idx_col in range(len(matrix)):
                temp.append(matrix[idx_col][idx_row])
            result.append(temp)
        
        

        return result