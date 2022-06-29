class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        getRow = -1
        for i in range(len(matrix)):
            if(matrix[i][0]<=target):
                getRow = i
            print(getRow)
        if(getRow==-1):
            return False
        for i in matrix[getRow]:
            if(i==target):
                return True
            if(i>target):
                return False
        