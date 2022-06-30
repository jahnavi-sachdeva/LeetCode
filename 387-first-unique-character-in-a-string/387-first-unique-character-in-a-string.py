from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = Counter(s)
        print(dict1)
        minIndex = len(s)
        for i in dict1.keys():
            if(dict1[i] == 1):
                minIndex = min(s.index(i), minIndex)
        if(minIndex == len(s)):
            return -1
        return minIndex