class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, num in enumerate(nums):
            if num >= target:
                return i
            if i == len(nums) - 1:
                return i + 1


if __name__ == '__main__':
    s = Solution()
    assert 2 == s.searchInsert([1, 3, 5, 6], 5)
    assert 1 == s.searchInsert([1, 3, 5, 6], 2)
    assert 4 == s.searchInsert([1, 3, 5, 6], 7)
    assert 0 == s.searchInsert([1, 3, 5, 6], 0)
