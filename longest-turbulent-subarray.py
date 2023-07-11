class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l ,r = 0,1
        mx , pre = 1,""
        while r < len(arr):
            if arr[r-1] > arr[r] and pre != ">":
                mx = max(mx,r-l+1)
                r += 1
                pre = ">"
            elif arr[r-1] < arr[r] and pre != "<":
                mx = max(mx,r-l+1)
                r += 1
                pre = "<"
            else:
                r = r+1 if arr[r-1] == arr[r] else r
                l = r-1
                pre =""        
        
        return mx