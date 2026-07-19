class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 2:
            return x

        temp = x / 2.0

        while True:
            checkTemp = (temp + (x / temp)) / 2.0
            checkRes = abs(checkTemp - temp)

            if checkRes < 1e-6:
                return int(checkTemp)

            temp = checkTemp