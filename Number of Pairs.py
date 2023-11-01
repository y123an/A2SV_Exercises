import bisect
t = int(input())
for _ in range(t):
    n, l, r = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()
    c = 0
    for i in range(n):
        idx = bisect.bisect_left(arr, l - arr[i], i + 1)
        idx2 = bisect.bisect_right(arr, r - arr[i], i + 1)
        c += idx2 - idx
    print(c)
