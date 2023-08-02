import math

t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    c=min(a,b);
    d=(a+b)//4;
    if(a==b):
        print(math.floor(a/2))
    else:
        print(min(c,d))