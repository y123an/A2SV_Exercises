class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = 0
        en = 0
        max = 0
        sub = set()
        while en < len(s):
            if s[en] in sub:
                sub.remove(s[st]) 
                st +=1
            else:
                leng = en-st+1
                if max < leng:
                    max = leng
                sub.add(s[en])
                en +=1
        
        return max