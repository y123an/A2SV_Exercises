class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ana = collections.Counter(p)
        c_ana = collections.Counter()
        
        if len(p) >len(s):
            return []
        
        for i in range(len(p)):
            c_ana[s[i]] += 1
        
        l = 0
        r = len(p) -1
        ans = []
        if ana == c_ana:
            ans.append(l)
        while r < len(s)-1:
            c_ana[s[l]] -= 1
            l += 1
            r += 1
            c_ana[s[r]] += 1
            if ana == c_ana:
                ans.append(l)

        return ans 
