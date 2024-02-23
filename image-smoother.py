# time complexity = O(n*m)
# space complexity = O(n*m)

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row, col = len(img), len(img[0])

        # creating a metrix using list compresion
        res = [[0] * col for _ in range(row)]

        # itrating through the cells one by one 
        for r in range(row):
            for c in range(col):
                total = 0
                cnt = 0
                
                # checking the corrosponding 8 elements for every cell if exists
                for i in range(r-1 , r+2):
                    for j in range(c-1, c+2):

                        # checking if the cell exists to avoid out of index bound
                        if i < 0 or i == row or j < 0 or j == col:
                            continue
                        total += img[i][j]
                        cnt += 1

                # calculating the avarage and assign it to its cell 
                res[r][c] = total // cnt
        
        return res