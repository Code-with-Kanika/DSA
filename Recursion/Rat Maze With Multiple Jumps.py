'''
A maze is given as n*n matrix of blocks where source block is the upper left most block i.e., matrix[0][0] and destination block is lower rightmost block i.e., matrix[n-1][n-1]. A rat starts from source and has to reach the destination.
The rat can move in only two directions: first forward (if possible) or down.
In the maze matrix, 0 means the block is the dead end and non-zero number means the block can be used in the path from source to destination. The non-zero value of mat[i][j] indicates number of maximum jumps rat can make from cell mat[i][j]. 
Return a maxtrix of size n*n in which 1 at (i, j) represents the cell is taken into the path otherwise 0 .

Note : If multiple solutions exist, the shortest earliest hop will be accepted. For the same hop distance at any point, forward will be preferred over downward. 

Shortest > Forward > Downward

Input: {{2,1,0,0},{3,0,0,1},{0,1,0,1},
{0,0,0,1}}
Output: {{1,0,0,0},{1,0,0,1},{0,0,0,1},
{0,0,0,1}}

Input: {{2,1,0,0},{2,0,0,1},{0,1,0,1},
{0,0,0,1}}
Output: {{-1}}
'''

def ShortestDistance(mat):
    n,m =len(mat),len(mat[0])
    dp =[[0]*m]*n


    def rec(i,j):
        if i==n-1 and j==m-1 : 
            dp[i][j]=1
            return True

        if i < 0 or i >= n or j < 0 or j >= m or mat[i][j] == 0:
            return False
        
        if dp[i][j] == 1:  # Avoid revisiting the same cell
            return False
        
        valueToMove = mat[i][j]
        dp[i][j]=1
        for v in range(valueToMove):
            if j+v < m and rec(i,j+v) :
                return True
            
            if i+v < n and rec(i+v,j):
                return True
        
        dp[i][j] = 0
        return False
    
    if rec(0,0) :
        return dp
    else:
        return [[-1]]
    
####################DP######################## 
def ShortestDistanceDP(mat):
    n, m = len(mat), len(mat[0])
    dp = [[0] * m for _ in range(n)]  # Initialize the solution matrix
    store = [[-1] * m for _ in range(n)] 
        
    def rec(i, j):
        # Check if we're adjacent to the destination
        if (i == n - 1 and j == m - 1) :
            store[i][j] = True
            dp[i][j] = 1
            return True
                
        if i < 0 or i >= n or j < 0 or j >= m or mat[i][j] == 0:
            return False
    
    
        if store[i][j] != -1:
            return store[i][j]
                
        dp[i][j] = 1
        valueToMove = mat[i][j]
        result=False
            
        # Try all forward moves within bounds
        for v in range(1, valueToMove + 1):
            if j + v < m and rec(i, j + v):
                result= True
                return True
    
            if i + v < n and rec(i + v, j):
                result= True
                return True
            
        store[i][j] = result
        # If no path works, backtrack
        if not result:
            dp[i][j] = 0
            
        return store[i][j]
    
    # Start the recursive solution from the top-left corner
    if rec(0, 0):
        return dp
    else:
        return [[-1]]


