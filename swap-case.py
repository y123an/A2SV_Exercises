def swap_case(s):
    ans = ""
    
    for x in s:
        if x == x.upper():
            ans += x.lower()
        else:
            ans += x.upper()
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)