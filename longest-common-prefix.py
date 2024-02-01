class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        sorted_str = sorted(strs)
        first = sorted_str[0]
        last = sorted_str[-1]

        print(sorted_str)
        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
             
        return ans