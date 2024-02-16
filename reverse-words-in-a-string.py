class Solution:
    def reverseWords(self, s: str) -> str:
        arrS = s.split(" ")
        arr = []
        for i in range(len(arrS)):
            if arrS[i] != "":
                arr.append(arrS[i])
        l, r =0, len(arr) -1
        while l < r:
            arr[l],arr[r] = arr[r],arr[l]
            l += 1
            r -= 1
        return " ".join(arr)