if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_arr = sorted(arr)
    a = sorted_arr[-1]
    
    for x in sorted_arr[::-1]:
        if x != a:
            print(x)
            break
