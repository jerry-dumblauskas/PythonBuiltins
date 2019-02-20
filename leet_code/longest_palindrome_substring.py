"""
leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    pala = ""

    def longestPalindrome(self, s: 'str') -> 'str':

        for my_left in range(len(s)):
            str_len = len(s)
            if len(self.pala) > (str_len - my_left):
                break
            while str_len > my_left:
                if len(self.pala) > (str_len - my_left):
                    break
                if Solution.isPalindrome(s[my_left:str_len]):
                    if len(s[my_left:str_len]) > len(self.pala):
                        self.pala = s[my_left:str_len]
                str_len -= 1

        return self.pala

    @staticmethod
    def isPalindrome(x):
        st = 0
        end = len(x) - 1
        while st < end:
            if x[st] != x[end]:
                return False
            st += 1
            end -= 1
        return True


if __name__ == '__main__':
    sol = Solution()
    #print(sol.longestPalindrome("rgczcpratwyqxaszbuwwcadruayhasynuxnakpmsyhxzlnxmdtsqqlmwnbxvmgvllafrpmlfuqpbhjddmhmbcgmlyeypkfpreddyencsdmgxysctpubvgeedhurvizgqxclhpfrvxggrowaynrtuwvvvwnqlowdihtrdzjffrgoeqivnprdnpvfjuhycpfydjcpfcnkpyujljiesmuxhtizzvwhvpqylvcirwqsmpptyhcqybstsfgjadicwzycswwmpluvzqdvnhkcofptqrzgjqtbvbdxylrylinspncrkxclykccbwridpqckstxdjawvziucrswpsfmisqiozworibeycuarcidbljslwbalcemgymnsxfziattdylrulwrybzztoxhevsdnvvljfzzrgcmagshucoalfiuapgzpqgjjgqsmcvtdsvehewrvtkeqwgmatqdpwlayjcxcavjmgpdyklrjcqvxjqbjucfubgmgpkfdxznkhcejscymuildfnuxwmuklntnyycdcscioimenaeohgpbcpogyifcsatfxeslstkjclauqmywacizyapxlgtcchlxkvygzeucwalhvhbwkvbceqajstxzzppcxoanhyfkgwaelsfdeeviqogjpresnoacegfeejyychabkhszcokdxpaqrprwfdahjqkfptwpeykgumyemgkccynxuvbdpjlrbgqtcqulxodurugofuwzudnhgxdrbbxtrvdnlodyhsifvyspejenpdckevzqrexplpcqtwtxlimfrsjumiygqeemhihcxyngsemcolrnlyhqlbqbcestadoxtrdvcgucntjnfavylip"))
    print(sol.isPalindrome("abXba"))