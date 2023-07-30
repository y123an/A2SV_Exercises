class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p , s in zip(position,speed)]

        stack = []

        for p , s in sorted(pairs)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack) 





                                #   stack = [1,7,12]             target = 12
                                #   p = [10,8,5,3,0]
                                #   s = [2,4,1,3,1]
                                #                |