class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        s = {}
        def solve(l,r,p):
            if (l,r,p) in s: return s[(l,r,p)]
            if l>r:
                return 0
            
            if p : s[(l,r,p)] = max(nums[l] + solve(l+1,r,not p),nums[r] + solve(l,r-1,not p))
            else: s[(l,r,p)] = min(-nums[l] + solve(l+1,r,not p),-nums[r] + solve(l,r-1,not p))
            
            return s[(l,r,p)]
        return solve(0,len(nums)-1,True) >= 0