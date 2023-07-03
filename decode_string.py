class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                sub = ""
                while stack[-1] != '[':
                    sub = stack[-1] + sub
                    stack.pop()
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack[-1] + k
                    stack.pop() 
                
                stack.append((sub) * int(k))

        return "".join(stack)
        