'''
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

"Concept- Take/Not Take - with Repetetiveness"
'''

def combinationSum(candidates, target):
        n=len(candidates)
        ans=[]
        def dfs(i,gp,target):
            if i >= n or target <0 :
                return                 
            
            if target == 0 :
                ans.append(gp[::])
                return 
            
            dfs(i,gp+[candidates[i]],target- candidates[i])
            
            dfs(i+1,gp, target)
        
        dfs(0,[],target)

        return ans

