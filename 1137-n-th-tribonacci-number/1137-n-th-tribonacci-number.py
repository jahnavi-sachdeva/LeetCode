class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n==0):
            return 0
        elif(n==1):
            return 1
        elif(n==2):
            return 1
        else:
            fib = [0,1,1]
            for i in range(3,n+1):
                fib.append(fib[i-1]+fib[i-2]+fib[i-3])
                # print(i,fib)
            return fib[-1]
        