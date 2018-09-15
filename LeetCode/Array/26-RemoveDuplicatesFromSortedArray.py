class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)