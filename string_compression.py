class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        r = 0
        c_c = None
        cnt = 0

        while r < len(chars):
            c = chars[r]
            r += 1

            if c == c_c:
                cnt +=1
            else:
                if c_c is not None:
                    chars[l] = c_c
                    l +=1
                if cnt >1:
                    for x in str(cnt):
                        chars[l] = x
                        l += 1
                c_c = c
                cnt = 1
        
        if c_c is not None:
            chars[l] = c_c
            l +=1
            if cnt >1:
                for x in str(cnt):
                    chars[l] = x
                    l += 1
        
        return l

            

            

         