class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1 = ""  
        string2 = ""

        # adding the array of word to their corrosponding variabels
        for x in word1:
            string1 += x

        for x in word2:
            string2 += x

        return string1 == string2
  
        