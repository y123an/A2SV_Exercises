class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for x in s:
            if x == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        
        s1 = "".join(stack)
        stack = []
        for x in t:
            if x =='#':
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        
        s2 = "".join(stack)
        return True if s1 == s2 else False