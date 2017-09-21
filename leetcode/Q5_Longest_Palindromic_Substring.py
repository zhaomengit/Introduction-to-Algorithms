class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lens = len(s)
        if lens <= 2:
            return s
        maxLen = -1
        start = 0
        for i in range(lens):
            low = i
            high = i

            while low >= 0 and high + 1 < lens and s[high] == s[high + 1]:
                high += 1

            while low >= 0 and high < lens and s[low] == s[high]:
                low -= 1
                high += 1

            if high - low - 1 > maxLen:
                maxLen = high - low -1
                start = low + 1

        return s[start:start+maxLen]
