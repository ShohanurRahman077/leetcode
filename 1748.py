from collections import defaultdict
def sumOfUnique(nums):
    uniqueSet = defaultdict(int)
    sum = 0
    for x in nums:
        uniqueSet[x] +=1
        
    for y in uniqueSet:
        if(uniqueSet[y]==1):
            sum+=y
    return sum

print(sumOfUnique([1,2,3,2]))