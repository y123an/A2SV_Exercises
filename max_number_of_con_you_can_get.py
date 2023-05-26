class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i=0
        j=len(piles)-2
        sum=0

        while(i<len(piles)/3):
            i += 1
            sum += piles[j]
            j -=2
        
        return sum