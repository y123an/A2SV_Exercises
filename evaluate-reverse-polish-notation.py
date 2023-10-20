class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        A = tokens
        for i  in range(len(tokens)):
            if A[i] != "+" and A[i] != "-" and A[i] != "/" and A[i] != "*":
                s.append(int(A[i]))
                continue
            else:
                b = s.pop()
                a = s.pop()
                if (A[i] == "+"):
                    s.append(a + b)
                elif (A[i] == "-"):
                    s.append(a - b)
                elif (A[i] == "*"):
                    s.append(a * b)
                else:
                    s.append(int(a / b))
        
        
        return s[-1]
