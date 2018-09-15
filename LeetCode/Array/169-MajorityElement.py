class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        max_num = -1
        max_count = -1
        for num in count:
            if count[num] > max_count:
                max_count = count[num]
                max_num = num
        return max_num