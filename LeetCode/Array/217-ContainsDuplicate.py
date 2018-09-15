class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = {}
        res = False
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                res = True
                break
        return res
