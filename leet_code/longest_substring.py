class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = []
        l_rtn_cnt = 0
        rtn_cnt = 0

        for i, item in enumerate(s):
            if item not in lst:
                l_rtn_cnt += 1
                lst.append(item)
            else:
                for x in range(lst.index(item) + 1):
                    lst.pop(0)
                lst.append(item)
                l_rtn_cnt = len(lst)

            if l_rtn_cnt > rtn_cnt:
                rtn_cnt = l_rtn_cnt
        return rtn_cnt



if __name__ == '__main__':
    s = Solution()
    ss = ["abcabcbb", "q", "bbbbb", "pwwkew", "aab", "dvdf", "abba"]

    for it in ss:
        print(it, s.lengthOfLongestSubstring(it))
