class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        f = 0
        up = False
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                t = (digits[i] + f + 1) % 10
            else:
                t = (digits[i] + f) % 10
            if t != 0 or digits[i] == 0:
                digits[i] = t
                f = 0
            else:
                digits[i] = 0
                f = 1
                if i == 0:
                    up = True
        if up:
            return [1] + digits
        else:
            return digits
