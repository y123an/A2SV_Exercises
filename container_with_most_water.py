class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxr = 0
        while l < r:
            h = min(height[l],height[r])
            maxr = max(maxr , h * (r-l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return maxr