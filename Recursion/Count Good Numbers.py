'''
A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".

Input: n = 4
Output: 400

'''

def countGoodNumbers(self, n):

    mod = 10**9 + 7
    odd_places = n //2 
    even_places = n - odd_places
    return (pow(5, even_places, mod) * pow(4, odd_places, mod)) % mod


#Incase you need to find the list of numbers also.

def goodNumbers(n):
    out=[]
    odds="2357"
    even="02468"
    def rec(i,gp):
        if i==n:
            out.append(gp)
            return 
            
        if i%2 ==0:
            for j in even:
                rec(i+1, gp+ j)
        else:
            for k in odds:
                rec(i+1,gp+ k)
            
        
    rec(0,"")
    print(out)
    

