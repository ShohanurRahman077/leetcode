def subString(s,t):
    print (s,t)
    i , j = 0,0
    res = 0
    while i<len(s) and j< len(t):
        print (i,j)
        if s[i] == t[j]:
            i += 1
            res +=1
        
        j +=1
    return len(s) == 3        


subString("ayc","ahbdgc")