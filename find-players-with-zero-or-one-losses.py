# time complexity = n logn
# space complexity = o(n)
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hash_map = collections.Counter()
        has_zero_loss = []
        has_one_loss = []
        new_arr = set()
        for x in matches:
            hash_map[x[1]] += 1 
            new_arr.add(x[0])
            new_arr.add(x[1])

        for x in new_arr:
            if hash_map[x] == 0:
                has_zero_loss.append(x)
            if hash_map[x] == 1:
                has_one_loss.append(x)
        
        return [sorted(has_zero_loss),sorted(has_one_loss)]
