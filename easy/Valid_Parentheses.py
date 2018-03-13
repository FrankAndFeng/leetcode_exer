class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        stack = []
        dict1 = {'(': ')', '[': ']', '{': '}'}
        for i in range(0, length):
            if s[i] in dict1.keys():
                stack.append(s[i])
            elif s[i] in dict1.values():
                if stack == [] or dict1[stack[-1]] != s[i]:
                    return False
                else:
                    stack.pop()

        if stack == []:
            return True
        else:
            return False

if __name__ == '__main__':
    string = "([)]"
    s =Solution()
    print("%s is valid? %s" % (string, s.isValid(string)))