class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        runningSum = 0

        for i in range(len(nums)):
            runningSum = runningSum + nums[i]
            result.append(runningSum)
        
        return result
