'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice,
and the combinations may be returned in any order.


Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
'''

def combinationSum3(k, n):
    
    out=[]

    def rec(i,gp):
        sum_gp = sum(gp)
        len_gp = len(gp)
        if sum_gp == n and len_gp == k:
            out.append(gp)
            return 

        if i==10 or sum_gp>n or len_gp >k :
            return 
            
        rec(i+1,gp+[i])
        rec(i+1,gp)
        
    rec(1,[])
    return out 

