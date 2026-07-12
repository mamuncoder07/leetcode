class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        currentAltitude = 0
        highest = 0
        for i in range(len(gain)):
            currentAltitude =currentAltitude + gain[i]
            if currentAltitude > highest:
                highest = currentAltitude
            
        return highest