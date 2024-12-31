
# Bracket Challege (Extension of Generate Parenthesis) :
''' The first line of input consists of two integers,
N  - the number of parentheses and 
M - the number of braces pair.
Sample Input 0
1 2
Sample Output 0
(){}{}
{}(){}
{}{}()
(){{}}
{{}}()
{}{()}
{}({})
{()}{}
({}){}
(){{}}
{{}}()
{{()}}
{({})}
({{}})
({}{})
{(){}}
{{}()}
'''
from collections import deque 
n,m = map(int, input().split()) 
ans=set() 
st=deque() 

def rec(open_n,close_n,open_m,close_m,s):
    if open_n == 0 and close_n ==0 and open_m == 0 and close_m == 0:
        ans.add(s)
        return

    if open_n >0:
        s += "("
        st.append("(")
        rec(open_n-1,close_n,open_m,close_m,s)
        st.pop()
        s=s[:-1]

    if close_n > open_n and st and st[-1] == "(" :
        s+=")"
        st.pop()
        rec(open_n,close_n-1,open_m,close_m,s)
        s=s[:-1]
        st.append("(")

    if open_m >0:
        s += "{"
        st.append("{")
        rec(open_n,close_n,open_m-1,close_m,s)
        st.pop()
        s=s[:-1]

    if close_m > open_m and st and st[-1] == "{" :
        s+="}"
        st.pop()
        rec(open_n,close_n,open_m,close_m-1,s)
        s=s[:-1]
        st.append("{")
rec(n,n,m,m,"") 
for i in ans:
    print(i)