class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        sum = 0
        q = deque()
        mi = float('inf')
        r = 0

        while r < len(nums):
            sum += nums[r]
            if sum >= k:
                mi = min(mi, r+1)
            curr = ()
            while q and sum - q[0][1] >= k:
                curr = q[0]
                q.popleft()

            if curr:
                mi = min(mi,(r-curr[0]))
            
            while q and sum <= q[-1][1]:
                q.pop()

            q.append((r,sum))
            
            r += 1 
            


        return -1 if mi == float('inf') else mi
            
