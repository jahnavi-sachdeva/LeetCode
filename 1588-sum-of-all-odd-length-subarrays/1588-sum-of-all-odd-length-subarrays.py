class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        totalSum = 0
        for i in range(len(arr)):
            start = len(arr)-i
            end = i+1
            total = start * end
            occurance = 0
            if(total%2 == 0):
                occurance = total//2
            else:
                occurance = total //2 + 1
            totalSum+= arr[i]* occurance
        return totalSum
                