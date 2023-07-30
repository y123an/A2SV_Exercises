class Solution:
  def sumSubarrayMins(self, arr: List[int]) -> int:
    kMod = 1_000_000_007
    n = len(arr)
    ans = 0
    # prevMin[i] := index k s.t. arr[k] is the prev min in arr[:i]
    prevMin = [-1] * n
    # nextMin[i] := index k s.t. arr[k] is the next min in arr[i + 1:]
    nextMin = [n] * n
    stack = []

    for i, a in enumerate(arr):
      while stack and arr[stack[-1]] > a:
        index = stack.pop()
        nextMin[index] = i
      if stack:
        prevMin[i] = stack[-1]
      stack.append(i)

    for i, a in enumerate(arr):
      ans += a * (i - prevMin[i]) * (nextMin[i] - i)
      ans %= kMod

    return ans


    # prev = [-1,-1,-1,-1]              arr = [3,1,2,4]  index = 1
    # next = [4,4,4,4]                           |

    # stack = [0]










