class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if nums2 != []:
            nums3 = []
            i, j = 0, 0
            while j < m:
                if nums2[i] > nums1[j]:
                    nums3.append(nums1[j])
                    j += 1
                else:
                    nums3.append(nums2[i])
                    i += 1
                    if i == n:
                        break
                print nums3
            if j < m:
                for k in range(j, m):
                    nums3.append(nums1[k])
            if i < n:
                for k in range(i, n):
                    nums3.append(nums2[k])
            nums1[:] = nums3