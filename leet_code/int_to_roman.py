class Solution:

    def intToRoman(self, num):
        roman_list = ["M","CM","D", "CD", "C", "XC","L","XL","X", "IX", "V", "IV","I"]
        integ_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5,4,1]

        rtn = ""

        for val in integ_list:
            while num >= val:
                num = num - val
                ind = integ_list.index(val)
                rtn = rtn + roman_list[ind]

        return  rtn


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(20))
