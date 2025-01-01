'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

'''

class Solution:
    def solveNQueens(self, n):
        board=[["."]*n for i in range(n)]
        col=set()
        posDiag = set()
        negDiag=set()
        res=[]

        def rec(r):
            if r==n:
                c= ["".join(k) for k in board]
                res.append(c)
                return
                            
            for c in range(n):
                if c in col or r+c in posDiag or r-c in negDiag :
                    continue
                
                board[r][c] = "Q"
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                rec(r+1)
                board[r][c] = "."
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
        

        rec(0)
        return res
