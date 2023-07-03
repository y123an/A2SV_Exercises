class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill) -1
        sum = 0
        prev = None
        while l<r:
            prod = skill[l] + skill[r]
            if prev == None or prod == prev:
                sum += skill[l] * skill[r]
                prev = prod
                l +=1
                r -=1
            else:
                return -1
        return sum