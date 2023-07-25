def nextGreaterElement(nums1,nums2):
    ans = []
    stack = []
    map = {}
    for x in nums2:
        while (stack and x > stack[-1]):
            map[stack.pop()] = x
        stack.append(x)
    for x in nums1:
        if x in map:
            ans.append(map[x])
        else:
            ans.append(-1)
    return ans

print (nextGreaterElement( [2,4], [1,2,3,4]))