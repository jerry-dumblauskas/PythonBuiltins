class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = 0
        while True:
            if i == len(nums):
                break
            if nums[i] == val:
                nums.pop(i)
                i-=1
            i+=1

        return len(nums)


if __name__ == '__main__':
    s = Solution()
    x = [3,3]
    print(s.removeElement(x, 3))
    print(x)