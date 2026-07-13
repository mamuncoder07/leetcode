class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left = 0

        for i, x in enumerate(nums):
            if left == total - left - x :
                return i

            left += x
        
        return - 1