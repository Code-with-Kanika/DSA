
'''
Power of 2 - ans-2**n
'''
######################
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n<1:
            return False
        if n==1:
            return True
        
        return self.isPowerOfTwo(n/2)
        
#########################
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        cnt = bin(n).count('1')
        return cnt == 1

##########################
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
