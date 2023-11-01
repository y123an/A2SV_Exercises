class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        c =  0
        for i in range(len(arr) - 1):
            x = arr[i]
            for j in range(i+1,len(arr)):
                x ^= arr[j]
                if x == 0:
                    c += j-i
        return c