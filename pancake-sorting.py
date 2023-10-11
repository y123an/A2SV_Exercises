class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []

        def flip(index):
            for i in range(0, index//2 + 1):
                temp = arr[i]
                arr[i] = arr[index-i]
                arr[index-i] = temp

        for i in range(len(arr)-1,0,-1):
            for j in range(1, i+1):
                if arr[j] == i+1:
                    flip(j)
                    res.append(j+1)
                    break
            flip(i)
            res.append(i+1)

        return res
        