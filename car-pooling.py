class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        maxi =sorted(trips, key=lambda x: x[2])
        arr = [0]*maxi[-1][2]


        for x in trips:
            for i in range(x[1]-1,x[2]-1):
                arr[i] = arr[i] + x[0]

        for x in arr:
            if x > capacity:
                return False

        return True