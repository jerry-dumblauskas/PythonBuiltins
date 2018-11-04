class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ar_len=len(nums)
        for i, value in enumerate(nums):
            if (i + 1) < ar_len:
                if value > nums[i + 1]:
                    return i
        return i



if __name__ == '__main__':
    s = Solution()
    sample = [1,2]
    print (s.findPeakElement(sample))
