class DataStream:

    def __init__(self, value: int, k: int):
        self.q = deque()
        self.val = value
        self.k = k
        self.cnt = collections.Counter()

    def consec(self, num: int) -> bool:
        self.q.append(num)

        if num == self.val: self.cnt[num] += 1

        while len(self.q) > self.k:
            x = self.q.popleft()
            self.cnt[x] -= 1
            if self.cnt[x] == 0:
                del self.cnt[x]

        return self.cnt[num] == self.k        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)