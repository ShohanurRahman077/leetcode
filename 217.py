from collections import defaultdict
def containsDuplicate(nums):
    counts = defaultdict(int)
    for x in nums:
        counts[x] +=1
        if counts[x]>=2:
            return True
    return False
    




print(containsDuplicate([1,2,3]))