'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations 
in any order.

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
'''

def permuteUnique(nums):
        out=[]
        nums.sort()
        
        def rec(nums , gp):
            if not nums :
                out.append(gp)

            for i in range(len(nums)):
                if i>0 and nums[i-1] == nums[i]: # Skipping same procedure for duplicate number.
                    continue
                rec(nums[:i]+ nums[i+1:], gp+[nums[i]])

        rec(nums , [])
        return out
