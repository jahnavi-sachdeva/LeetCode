from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomDict = Counter(ransomNote)
        magDict = Counter(magazine)
        
        for i in ransomDict.keys():
            if( i not in magDict.keys()):
                return False
            elif( ransomDict[i]>magDict[i]):
                return False
            
        return True