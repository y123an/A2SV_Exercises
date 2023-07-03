class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def powr(x):
            if x == 1:
                return True
            elif x % 3 == 0 and x != 0:
                return powr(x/3)
            else:
                return False
                
        
        return powr(n)

        