class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        res = []
        arr = []
        if(m*n == r*c):
            for i in range(m):
                for j in range(n):
                    if(len(arr)==c):
                        res.append(arr)
                        arr = []
                    arr.append(mat[i][j])
                print(arr)
                print(res)
            res.append(arr)
            return res
        return mat
        