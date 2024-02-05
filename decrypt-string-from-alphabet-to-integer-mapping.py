class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ""
        counter = len(s) -1

        #iterating through the string backward
        while counter >= 0:

            # if we find #  we will take the next 2 element and map it to the character
            if s[counter] == '#'
                result += chr(int(s[counter-2:counter])+96)
                counter -= 3
            else:
                result += chr(int(s[counter])+96)
                counter -= 1

        return result[::-1]