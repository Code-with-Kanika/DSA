'''
We have N persons sitting on a round table. Any person can do a handshake with any other person.

In how many ways these N people can make handshakes so that no two handshakes cross each other. N would be even. 

N = 2 Output: 1
N = 4 Output: 2
'''

class Solution:
    def count(self, N):
        hmap={0:1,2:1}
        
        if N%2!=0:
            return 0
        
        def rec(i):
            if i in hmap :
                return hmap[i]
            
            if i%2!=0:
                return 0

            sumi=0
            for j in range(i):
                sumi += rec(j) * rec(i-2-j)
            
            hmap[i] = sumi
            return sumi
        
        return rec(N)


################ DP ###################

def f(N):
    dp=[0]*(N+1)
    dp[2]=1
    dp[0]=1

    for i in range(3,N+1):
        sumi=0
        for j in range(i):
            sumi += dp[j] * dp[i-2-j]
        
        dp[i] = sumi
    
    return dp[N]
    


        
