#Find nth fibonacci number.
'''
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
'''
def fib(self, n):
        if n<2:
            return n
        
        a,b=0,1

        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        
        return c

