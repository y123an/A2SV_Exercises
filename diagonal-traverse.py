class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if (len(mat) == 1):
            return mat[0]
        
        res = []
        up = True
        
        i , j = 0, 0

        row = len(mat)
        col = len(mat[0])

        while i < row and j < col:
            if up:
                while i >  0 and j < col-1:
                    res.append(mat[i][j])
                    i -= 1
                    j += 1
                res.append(mat[i][j])
                up = False
                if j == col-1:
                    i += 1
                else:
                    j += 1
            else:
                while i < row-1 and j > 0:
                    res.append(mat[i][j])
                    i += 1
                    j -= 1
                res.append(mat[i][j])
                up = True
                if i == row-1:
                    j += 1
                else:
                    i += 1

        return res