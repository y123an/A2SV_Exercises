# here is the take action is defined
def calculate(x, y, z, n):
    result = [[i,j,k] for i in range(x+1)  for j in range(y+1)  for k in range(z +1) if i+j+k != n]
    
    return result


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    #take action
    print(calculate(x,y,z,n))