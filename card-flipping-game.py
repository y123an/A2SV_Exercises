class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        sets = set(fronts + backs)

        for f,b in zip(fronts, backs):
            if f == b:
                sets.discard(f) # need discard instead of remove. ex. [1,1], [1,1]
        
        return min(sets, default = 0)