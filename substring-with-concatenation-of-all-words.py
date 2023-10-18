class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        res = []
        count = collections.Counter()
        wl = len(words[0])
        wsl = len(words) * wl

        for x in words:
            count[x] += 1
        l = 0
        r = wsl   
        while r <= len(s):
            wordseen = collections.Counter()
            word = ""
            
            for i in range(l,r):
                word += s[i]
                if len(word) == wl:
                    wordseen[word] += 1
                    word = ""
            if wordseen == count:
                res.append(l) 
            r  += 1
            l += 1