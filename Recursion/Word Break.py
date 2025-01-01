'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a 
space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true

Input: s = "aaaaaaaa", wordDict = ["aaaaa","aaa"]
Output: true
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        wordset=set(wordDict)
        n=len(s)
        dp = [False] * (n + 1)
        dp[0] = True 

        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordset :
                    dp[i] = True
                    break
                    
        return dp[n]
