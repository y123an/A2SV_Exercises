class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}

        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

      

        temp = sorted(freq.items(),key=lambda x:x[1],reverse= True)

        ans = ""

        for x, y in temp:
            while y:
                ans += x
                y -=1

        return ans