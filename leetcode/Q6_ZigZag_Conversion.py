class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = list()
        step = numRows + numRows - 2
        for x in xrange(numRows):
            k = x
            g = step - x
            #print "k is--", k, "g is--", g
            if x == 0 or x == numRows - 1:
                while k < len(s):
                    result.append(s[k])
                    k += step
            else:
                while k < len(s):
                    result.append(s[k])
                    if g < len(s):
                        result.append(s[g])
                        g += step
                    k += step

        return "".join(result)
