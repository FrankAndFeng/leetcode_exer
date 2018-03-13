from functools import reduce


class Solution:
    def lcp(self, str1, str2):
        """
        :type str1,str2:string
        :rtype: str, common prefix
        """
        j = 0
        for i in range(0, min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                j += 1
            else:
                break
        return str1[0:j]

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs:
            return reduce(self.lcp, strs)
        else:
            return ''

if __name__ == '__main__':
    strs = ["qwert", "qwertyu", "qwer"]
    s = Solution()
    print("longest common prefix:%s" % s.longestCommonPrefix(strs))
