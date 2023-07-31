class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1,max(piles)
        mini = float('inf')

        while l <= r:
            mid = (l + r)//2
            H = 0
            for x in piles:
                H += ceil(x/mid)   
            if H > h:
                l = mid + 1
            else:
                mini = min(mini,mid)
                r = mid - 1
        
        return mini
