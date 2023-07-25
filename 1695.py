from collections import deque,defaultdict
def maximumUniqueSubArray(nums: list[int]):
    left = sum = 0
    res = 0
    freq = defaultdict(int)
    for x in nums:
        sum +=x
        freq[x]+=1
        while freq[x]>1:
            sum -=nums[left]
            freq[nums[left]] -=1
            left +=1
        res = max(sum,res)
    return res    

maximumUniqueSubArray([5,2,1,2,5,2,1,2,5])
