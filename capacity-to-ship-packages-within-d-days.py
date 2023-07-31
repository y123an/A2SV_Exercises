class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        
        ans = 0
        while l <= r:
            mid = (l + r)//2
            D = 1
            total = 0
            for w in weights:
                total += w
                if total > mid:
                    D += 1
                    total = w
            
            if D > days:
                l = mid + 1
            else:
                ans = mid
                r = mid - 1

        return ans


