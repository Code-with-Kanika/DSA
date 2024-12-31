'''
N = 10
Output: 10 9 8 7 6 5 4 3 2 1
'''

class Solution:
    def printNos(self, n):
        
        if n==0:
            return
        
        print(n,end=" ")
        self.printNos(n-1)
        