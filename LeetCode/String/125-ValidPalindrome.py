class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        char_list = []
        for c in s:
            if c.isalpha() or c.isdigit():
                char_list.append(c)
        s = ''.join(char_list)
        for i in range(len(s) // 2):
            j = len(s) - i - 1
            #print s[i], s[j], (i, j)
            if s[i] != s[j]:
                return False
        return True