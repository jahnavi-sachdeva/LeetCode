class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n==0):
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        else:
            arr = [0,1,1]
            res = 1
            for i in range(3,n+1):
                if(i%2==0):
                    arr.append(arr[i//2])
                    res=max(arr[i//2],res)
                else:
                    arr.append(arr[i//2]+arr[(i//2)+1])
                    res=max(res,arr[i//2]+arr[(i//2)+1])
                print(arr)
            return res
                    