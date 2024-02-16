class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        arr = []
        
        for i, balls in enumerate(boxes):
            if balls == '1':
                arr.append(i)
        
        res = []
        for i in range(len(boxes)):
            tmp = 0
            for index in arr:
                tmp += abs(i - index)
            res.append(tmp)
            
        return res
    