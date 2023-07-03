class Solution:
    def isPowerOfFour(self, n: int) -> bool:
       
        def powr(x):
            if x == 1:
                return True
            elif x % 4 == 0 and x != 0:
                return powr(x/4)
            else:
                return False
                
        
        return powr(n)
