class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l_dict = {}
        for i in range(len(nums)):
            magic_test = target - nums[i]
            if magic_test in l_dict:
                return [l_dict[magic_test], i]
            l_dict[nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    nums = [3,2,4]
    print(s.twoSum(nums, 6))
