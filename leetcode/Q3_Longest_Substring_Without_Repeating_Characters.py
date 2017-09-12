# 使用一个dict保存已经访问过的,如果有重复的,重置下start,往后从start开始数
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        start = maxlen = 0
        for i in range(len(s)):
            if s[i] in d and start <= d[s[i]]:
                start = d[s[i]] + 1
            else:
                maxlen = max(maxlen, i - start + 1)

            d[s[i]] = i

        return maxlen
