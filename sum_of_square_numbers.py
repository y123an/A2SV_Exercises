class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <= 1: return True
        
        sqrs = set([a*a for a in range(int(sqrt(c))+1)])

        for a in sqrs:
            b = c - a
            if b in sqrs:
                return True
        return False
