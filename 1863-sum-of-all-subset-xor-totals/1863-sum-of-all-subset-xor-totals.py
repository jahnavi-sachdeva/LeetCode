import copy
class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mysubset = [[0]]
        
        def myfunc(subs):
            totSum = 0
            for sub in subs:
                print(sub)
                if sub:
                    zor = sub[0]
                    for i in range(1,len(sub)):
                        zor = zor ^ sub[i]
                    totSum+=zor
            print(totSum)
            return totSum
            
                
        def subsetsUtil(A, subset, index):
            mysubset.append(copy.copy(subset))
            for i in range(index, len(A)):
                subset.append(A[i])
                subsetsUtil(A, subset, i + 1)
                subset.pop(-1)
            return

        def subsets(A):
            subset = []     
            index = 0
            subsetsUtil(A, subset, index)

        array = nums
        subsets(array)
        print(mysubset)
        return myfunc(mysubset)
        # return totSum
        
        
                



        