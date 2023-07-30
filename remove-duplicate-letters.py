class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        feq = collections.Counter()
        seen =collections.Counter()
        stack = []
        for x in s:
            feq[x] += 1
            seen[x] = False
        
        for x in s:
            if seen[x]:
                feq[x] -= 1
                continue
            while stack and stack[-1] > x and feq[stack[-1]] > 0:
                seen[stack[-1]] = False
                stack.pop()
            stack.append(x)
            feq[x] -= 1
            seen[x] = True

        return "".join(stack)

    
    # bcabc
    #     |           
    #                 stack = [a,b,c]            
    #                 feq = {b : 0, c: 0, a: 0}
    #                 seen = {b: true, a:true, c:true}
        

