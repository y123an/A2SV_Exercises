t = int(input())
def sign(n):
    return n > 0

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    
    ans = 0
    i = 0
    while i < n:
        mx = arr[i]
        j = i
        while j < n and (sign(arr[i]) == sign(arr[j])):
            mx = max(mx,arr[j])
            j += 1
        ans += mx
        i = j
    print(ans)
            