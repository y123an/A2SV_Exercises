class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        c = collections.Counter(t)
        c2 = collections.Counter()

        have, need = 0,len(c)
        res, resL = [-1,-1],float("infinity")
        l = 0

        for r in range(len(s)):
            x = s[r]
            c2[x] += 1

            if x in c and c[x] == c2[x]:
                have += 1

            while have == need:
                if(r - l + 1) < resL:
                    res = [l,r]
                    resL = (r-l+1)
                
                c2[s[l]] -= 1

                if s[l] in c  and c2[s[l]] < c[s[l]]:
                    have -= 1
                l += 1

        l, r = res

        return s[l:r+1] if resL != float("inf") else "" 
