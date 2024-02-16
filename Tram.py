t = int(input())

n = 0

max_space = 0

for _ in range(t):
    a, b = map(int,input().split())
    n -= a
    n += b
    
    max_space = max(max_space,n)
    
    
print(max_space)