def goodPairs(nums):
    count = 0
    for x in range(len(nums)):
        for y in range(x+1, len(nums)):
            if nums[x] == nums[y]:
                count+=1
    return count



goodPairs( [1,1,1,1])