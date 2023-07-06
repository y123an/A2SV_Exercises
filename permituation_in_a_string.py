class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        cnt = collections.Counter(s1)
        cnt2 = collections.Counter()
        for i in range(len(s1)):
            cnt2[s2[i]] += 1
        
        l = 0
        r = len(s1) -1

        if cnt == cnt2:
            return True


        while r < len(s2)-1:
            cnt2[s2[l]] -= 1
            l += 1
            r += 1
            cnt2[s2[r]] +=1
            if cnt == cnt2:
                return True

        return False
            

        
        