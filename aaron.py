class Solution:
    def subsets(self, nums):
        rtn = []
        possibles = pow(2, len(nums))
        for i in range(possibles):
            mask = list(bin(i)[2:].zfill(len(nums)))
            lcl = []
            for a in range(len(nums)):
                if int(mask[a]):
                    lcl.append(nums[a])
            rtn.append(lcl)

        return rtn

if __name__ == '__main__':
    x = Solution()
    print(x.subsets([1,2,3]))