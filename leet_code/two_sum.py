class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for l, left in enumerate(nums):
            for r, right in enumerate(nums[1 + l:]):
                if target == left + right:
                    rtn = [l, r + 1 + l]
                    return rtn


if __name__ == '__main__':
    s = Solution()
    nums = [3,2,4]
    print(s.twoSum(nums, 6))
