class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        c = collections.Counter()
        count = 0
        ans = []
        st = ""
        for i in range(len(s)):
            if count < 10:
                st += s[i] 
            count += 1
        c[st] += 1
        r = 10
        l = 0
        while r < len(s):
            r += 1
            l += 1
            st = s[l:r]
            c[st] += 1
        for x in c:
            if c[x] >= 2:
                ans.append(x)

        return ans 
