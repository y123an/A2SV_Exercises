class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        l = 0
        r = 0 
        if len(players) == 1 or len(trainers) == 1:
            if players[-1] <= trainers[-1]:
                return 1
            else:
                return 0

        while players[l] > trainers[r]:
            r += 1
        c = 0
        while l < len(players) and r < len(trainers):
            if  players[l] <= trainers[r]:
                l += 1
                r += 1
                c += 1
            elif players[l] > trainers[r]:
                r += 1
        
        return c
            