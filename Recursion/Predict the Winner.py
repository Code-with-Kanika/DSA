'''
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.
Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. 
At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or 
nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their 
score. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still 
the winner, and you should also return true. You may assume that both players are playing optimally.

Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will
be left with 1 (or 2). So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return false.

## Very Imp Example:
Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
'''

def predictTheWinner(nums):
    def rec(i,j,lastP1):
        if i>j:
            return 0

        best=0
        if lastP1:
            best = rec(i+1,j,False) + nums[i] 
            best = max(best , rec(i,j-1,False) + nums[j])
        else:
            best = rec(i,j-1,True) - nums[j] 
            best = min(best , rec(i+1,j,True) - nums[i])
            
        return best
        
    return rec(0,len(nums)-1, True) >=0 


'''
Why Minimize Player 1's Potential Score?
The idea is rooted in the nature of optimal gameplay for both players:

Player 1's Goal: Maximize their score.
Player 2's Goal: Minimize Player 1's advantage (i.e., Player 2 doesn't necessarily maximize their score
but makes moves that result in the least favorable outcome for Player 1).
When Player 2 makes a move, they aren't directly maximizing their score. Instead, they strategically pick 
a number that leaves Player 1 with the least valuable options in future turns. This is why Player 2 minimizes
Player 1's potential score indirectly by choosing the lesser "evil" for themselves.
'''

