from collections import Counter
n = int(input())

hash_map = Counter()

for _ in range(n):
    name, number = input().split()
    hash_map[name] = number

while True:
    try:
        name = input()
        phone = hash_map.get(name, "Not found")
        if phone == "Not found":
            print("Not found")
        else:
            print(f"{name}={phone}")
            
    except EOFError:
        break
        