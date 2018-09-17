class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        last_str = ''
        for i in range(1, n + 1):
            index_str = ''
            if i == 1:
                index_str = '1'
                last_str = '1'
            else:
                count = 0
                last_c = last_str[0]
                for j, c in enumerate(last_str):
                    if c == last_c:
                        count += 1
                        if j == (len(last_str) - 1):
                            index_str += str(count) + str(last_c)
                    else:
                        index_str += str(count) + str(last_c)
                        count = 1
                        last_c = c
                        if j == (len(last_str) - 1):
                            index_str += str(count) + str(last_c)
                last_str = index_str
        return index_str

