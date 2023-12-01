class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key= lambda x: x[1])
        dic = {}
        passengers = 0
        for i in range(len(trips)):
            temp = []
            for j in dic:
                if j <= trips[i][1]:
                    passengers -= dic[j]
                    temp.append(j)
                    # dic.pop(j)
                    # break
            for k in temp:
                dic.pop(k)
            if trips[i][2] not in dic:
                dic[trips[i][2]] = trips[i][0]
            else:
                dic[trips[i][2]] += trips[i][0]
            
            passengers += trips[i][0]
            if passengers > capacity:
                return False
        return True
