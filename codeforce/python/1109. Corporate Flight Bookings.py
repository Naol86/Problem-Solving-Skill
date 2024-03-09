import numpy as np
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        lis = np.zeros(n,dtype="int32")
        for i in range(len(bookings)):
            lis[bookings[i][0]-1:bookings[i][1]] += bookings[i][2]
        # print(lis)
        return lis