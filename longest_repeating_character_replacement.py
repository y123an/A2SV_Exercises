class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.Counter()
        l=0
        maxi = 0

        for r in range(len(s)):
            count[s[r]] += 1

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -=1
                l +=1
            
            maxi = max(maxi,(r-l+1))
            
        return maxi