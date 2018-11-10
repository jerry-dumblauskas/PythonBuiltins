class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        lst_rev = list(str(x))
        lst_rev.reverse()
        return str(x) == "".join(lst_rev)


if __name__ == '__main__':
    s = Solution()
    x = -121
    print(s.isPalindrome(x))
