from collections import defaultdict
def medianOfTwoArray(nums1,nums2):
    for y in nums2:
        nums1.append(y)     
    n = len(nums1)
    sortedMergedArray = sorted(nums1)
    if n % 2 == 0:
        mid1 = sortedMergedArray[n // 2 - 1]
        mid2 = sortedMergedArray[n // 2]
        median = (mid1 + mid2) / 2
    else:
        median = sortedMergedArray[n // 2]
    return median
    

   
medianOfTwoArray( [1,1], [1,2])
