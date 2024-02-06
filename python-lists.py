if __name__ == '__main__':
    N = int(input())
    list_value = []
    
    # iterating through the number of inputs
    for _ in range(N):
        # taking the input as a string of list
        command = list(map(str,input().split()))
        
        # checking the first element of the input and performing the task
        if command[0] == 'insert':
            list_value.insert(int(command[1]),int(command[2]))
        elif command[0] == 'print':
            print(list_value)
        elif command[0] == 'remove':
            list_value.remove(int(command[1]))
        elif command[0] == 'append':
            list_value.append(int(command[1]))
        elif command[0] == 'sort':
            list_value.sort()
        elif command[0] == 'pop':
            list_value.pop()
        elif command[0] == 'reverse':
            list_value.reverse()