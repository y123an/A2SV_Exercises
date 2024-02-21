# space complexity = O(n)
# time complexity = O(n*k)

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque([x for x in range(1,n+1)])

        # while there are more the 1 element in the queue poping left and appending right to  make cycle
        while len(queue) > 1:

            for _ in range(k-1):
                queue.append(queue.popleft())

            queue.popleft()

        return queue[0]