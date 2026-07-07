class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)

        newNum = 0
        digitSum = 0

        for ch in s:
            if ch != '0':
                digit =int(ch)

                newNum = newNum * 10 + digit
                digitSum += digit

        return newNum * digitSum                
