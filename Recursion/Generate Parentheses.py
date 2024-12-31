'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]
'''

def generateParenthesis(self, n: int) :

    out=[]
    def rec(openCount,closeCount,gp):
        if openCount == closeCount == n:
            out.append(gp)
            return 
        
        if openCount <n :
            rec(openCount + 1 , closeCount , gp+"(") 
        
        if openCount>closeCount :
            rec(openCount,closeCount+1,gp+")")
    
    rec(0,0,"")
    return out