def isSubset( a1, a2, n, m):
    
    for x in a2:
        if x in a1:
            a1.remove(x)
            continue
        else:
            return 'No'
    
    return 'Yes'