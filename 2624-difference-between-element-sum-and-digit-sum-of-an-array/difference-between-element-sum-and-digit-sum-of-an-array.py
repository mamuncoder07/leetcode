class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_sum = 0
        digit_sum = 0

        for num in nums:
            element_sum += num

            x = num
            while x > 0:
                digit_sum += x % 10
                x //= 10

        return abs(element_sum - digit_sum)        