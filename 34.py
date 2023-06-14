class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = {}
        for x,y in enumerate(nums):
            r = target - y
            if r in answer:
                return [x, answer[r]] 
            else:
                answer[y] = x    

            
                    
            