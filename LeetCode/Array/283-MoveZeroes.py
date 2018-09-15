class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        new_nums = []
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                new_nums.append(nums[i])
            else:
                count += 1
        nums[:] = new_nums[:] + [0, ] * count
