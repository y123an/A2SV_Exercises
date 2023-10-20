class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        c = 0
        for x in s:
            if x == '(':
                stack.append(c)
                c = 0
            else:
                c = stack.pop() + max(c*2,1)
                
        
        return c
