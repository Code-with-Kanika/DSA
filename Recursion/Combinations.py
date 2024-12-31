#Combinations taken k at a time from n numbers.
'''
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Approach - Take /Not Take Concept
'''
def combine(n, k):

    out=[]
    nums=[(i+1) for i in range(n+1)]

    def rec(i,gp):
        len_gp=len(gp)
        if len_gp==k:
            out.append(gp)
            return

        if len_gp >k or i>=n:
            return 

        if n-i+1 >= k-len_gp : #Added for further optimization
            rec(i+1,gp+[nums[i]])
            rec(i+1,gp)
    
    rec(0,[])
    return out








