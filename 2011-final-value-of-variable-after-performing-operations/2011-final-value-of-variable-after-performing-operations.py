class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for ops in operations:
            if "+" in ops:
                x+=1
            else:
                x-=1
        return x
                
        