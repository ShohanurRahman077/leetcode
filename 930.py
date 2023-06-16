def numOfSubArrayWithSum(nums, goal):
    left = curr = ans =0
    if goal ==0:
        return int(len(nums)*(len(nums)+1)/2)
    for right in range(len(nums)):
        curr +=nums[right]
        while curr>=goal:
            
            curr -=nums[left]
            left +=1
            ans = max(ans, right -left+1)

    return ans



print(numOfSubArrayWithSum( [1,0,1,0,1], 2))