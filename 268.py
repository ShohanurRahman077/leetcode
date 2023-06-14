class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length =  len(nums)
        expectedSum = length*(length+1)/2
        sum = 0
        for i in nums:
            sum = sum+i
        return expectedSum-sum    
        