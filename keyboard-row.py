class Solution:
    def findWords(self, words: List[str]) -> List[str]:
         
         return [
            w
            for w in words
            if set(w.lower()).issubset(set("qwertyuiop"))
            or set(w.lower()).issubset(set("asdfghjkl"))
            or set(w.lower()).issubset(set("zxcvbnm"))
        ]
     