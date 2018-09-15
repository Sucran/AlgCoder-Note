class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum = 0
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): # Note i+1
                sum = nums[i] + nums[j]
                if sum == target:
                    res += [i, j]
                    return res

