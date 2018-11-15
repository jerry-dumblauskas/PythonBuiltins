class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = -2147483648
        high = 2147483647

        lst_str = list(str(x))
        if lst_str[0] == "-":
            lst_str.pop(0)
            lst_str.append("-")

        answer = int("".join(reversed(lst_str)))
        if (answer > high ) or (answer < low):
            answer = 0
        return  answer


if __name__ == '__main__':
    s = Solution()
    ss = 1534236469
    print(ss, s.reverse(ss))
