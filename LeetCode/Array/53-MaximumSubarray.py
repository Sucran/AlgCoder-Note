class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_n = -100000
        if len(nums) == 1:
            max_n = nums[0]
            return max_n
        sum_n = 0
        for i in range(len(nums)):
            sum_n += nums[i]
            if sum_n > max_n:
                max_n = sum_n
            if sum_n < 0:
                sum_n = 0
        return max_n