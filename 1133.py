def largestUniqueNumber(nums):
    frequencySet = {}
    for x in nums:
        frequencySet[x] = frequencySet.get(x,0) +1

    ans = sorted([key for key, value in frequencySet.items() if value ==1],reverse=True)
    
    if len(ans)>0:
        return ans[0]
    return -1
 

print(largestUniqueNumber([5,7,3,9,4,9,8,3,1]))