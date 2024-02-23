class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        res = "".join(map(str,digits))
        res = int(res) + 1
        res = list(map(int,str(res)))
       
        return res