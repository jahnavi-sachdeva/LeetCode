from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictS = Counter(s)
        dictT = Counter(t)
        maxi = max(dictS,dictT)
        mini = min(dictS,dictT)
        for i in maxi:
            if i not in mini:
                return False
            elif(dictS[i]!=dictT[i]):
                return False
        return True