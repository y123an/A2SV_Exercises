class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        if len(arr) <= 1: return True
        
        l = 0 
        r = 1
        
        while r < len(arr):
            if arr[l] > arr[r]:
                return False
            r +=1
            l +=1
            
        return True
