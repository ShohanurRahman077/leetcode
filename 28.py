def findFistOccurrence(haystack, needle):
    left = 0
    right = 0
    curr = ''
    while right <len(haystack):
        curr += haystack[right]
        print(curr,len(curr))
        while len(curr) == len(needle):
            if curr == needle:
                return left
            left +=1
            curr = curr[1:]
        right +=1

    return -1


print(findFistOccurrence("leetcode","leet0"))