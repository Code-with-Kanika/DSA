'''
Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Input: nums = [0]
Output: [[],[0]]
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        out=[]
        n=len(nums)
        nums.sort()
        def rec(i,gp):
            if i == n:
                out.append(gp)
                return
            
            rec(i+1,gp+[nums[i]])

            while i+1 < n and nums[i] == nums[i+1] :
                i+=1

            rec(i+1,gp)
        
        rec(0,[])
        return out
        