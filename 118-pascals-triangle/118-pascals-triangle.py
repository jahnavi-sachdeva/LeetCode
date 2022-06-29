class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(numRows):
            arr = []
            for j in range(i+1):
                print("here",i,j)
                if(i==j):
                    arr.append(1)
                elif(j==0):
                    arr.append(1)
                else:
                    arr.append(triangle[i-1][j]+triangle[i-1][j-1])
                print(arr)
            print("here in i")
            triangle.append(arr)
        return triangle
        