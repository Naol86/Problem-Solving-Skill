class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        a = 0
        b = 0
        ans = 0
        while(a < len(players) and b < len(trainers)):
            if players[a] <= trainers[b]:
                a+=1
                b+=1
                ans +=1
            else:
                a+=1
        return ans