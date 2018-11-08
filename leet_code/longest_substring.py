class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        rtn_cnt = 0
        l_rtn_cnt = 0
        l_ptr = 0
        candidate_dict = {}
        next_ptr = 0
        while l_ptr < len(s):
            if s[l_ptr] not in candidate_dict:
                candidate_dict[s[l_ptr]] = l_ptr
                l_rtn_cnt += 1
            else:
                candidate_dict = {}
                l_ptr = next_ptr
                next_ptr += 1
                l_rtn_cnt = 0
            if l_rtn_cnt > rtn_cnt:
                rtn_cnt = l_rtn_cnt

            l_ptr += 1

        return rtn_cnt


if __name__ == '__main__':
    s = Solution()
    ss = "q"
    print(s.lengthOfLongestSubstring(ss))
