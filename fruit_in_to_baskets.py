class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dictt = collections.Counter()
        l = 0
        r = 0
        mx = 0
        total = 0

        while r < len(fruits):
            dictt[fruits[r]] += 1
            total += 1
            while len(dictt) > 2:
                dictt[fruits[l]] -= 1
                total -= 1
                if not dictt[fruits[l]]:
                    del dictt[fruits[l]]
                l += 1
            
            mx = max(mx,total)
            r += 1

        return mx