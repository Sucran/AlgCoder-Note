class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        l = l[::-1]
        s = ''.join(l)
        return s