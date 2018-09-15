class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = [ [1]*i for i in range(1, numRows+1) ]
        for i in range(2, numRows):
            for j in range(1, len(output[i])-1):
                output[i][j] = output[i-1][j-1] + output[i-1][j]
        return output