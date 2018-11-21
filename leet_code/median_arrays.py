"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
"""
class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1) + len(nums2)
        new_arr = sorted(nums2 + nums1)
        if total_len % 2 == 0:
            return (new_arr[int(len(new_arr) / 2)] + new_arr[int(len(new_arr) / 2) - 1]) / 2
        else:
            return new_arr[int(len(new_arr) / 2)]


if __name__ == '__main__':
    s = Solution()
    sample1 = [1, 4, 5]
    sample2 = [2, 3]
    print(s.findMedianSortedArrays(sample1, sample2))