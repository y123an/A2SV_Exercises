class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def solve(x,n):
            if x == 0: 
                return 0
            if n == 0: 
                return 1

            ans = solve(x,n//2)
            ans = ans * ans
            return ans * x if n % 2 != 0 else ans

        res = solve(x,abs(n))
        return 1/res if n < 0 else res
           
    #done
          
        