"""
Write a method answer(x,y,n) which returns the number of possible ways
to arrange n rabbits of unique heights along an east to west line, so
that only x are visible from the west, and only y are visible from the
east. The return value must be a string representing the number in base 10.

If there is no possible arrangement, return "0".

The number of rabbits (n) will be as small as 3 or as large as 40
The viewable rabbits from either side (x and y) will be as small as 1
and as large as the total number of rabbits (n).

Test cases
==========

Inputs:
    (int) x = 2
    (int) y = 2
    (int) n = 3
Output:
    (string) "2"

Inputs:
    (int) x = 1
    (int) y = 2
    (int) n = 6
Output:
    (string) "24"
"""
from math import factorial


def answer_2(x,y,n):
    if (x + y > n + 1 or
    n < 3 or n > 40 or x < 1
    or y < 1 or (y==x==1)):
        return "0"
 
    arrs = Arrangements_2(x,y,n)
    return str(arrs.calculate())
 
class Arrangements_2():
 
    def __init__(self,x,y,n):
        self.x = x
        self.y = y
        self.n = n
        self.count = 0
        
    def calculate(self):
        self.count = self._calculate(self.x,self.y,self.n)
        return self.count
    
    def _calculate(self,x,y,n):
        
        if x + y - 1 == n:
            return self.simple_arrangements(x,y,n)
        
        if n == 2:
            return 1
        
        if x+y == 3:
            return factorial(n-2)
        
        if x > 1:
            x_term = self._calculate(x-1,y,n-1)
        else:
            x_term = 0
        
        if y > 1:
            y_term = self._calculate(x,y-1,n-1)
        else:
            y_term =0
        
        return x_term + y_term + self._calculate(x,y,n-1)*(n-2)
           

    def simple_arrangements(self,x,y,n):
        return factorial(n-1.)/factorial(x-1.)/factorial(y-1.)


def answer(x,y,n):
    if (x + y > n + 1 or
    n < 3 or n > 40 or x < 1
    or y < 1 or (y==x==1)):
        return "0"
        
    arrs = Arrangements(x,y,n)
    return str(int(arrs.calc()))
        
class Arrangements():
    
    def __init__(self,x,y,n):
        self.x = x
        self.y = y
        self.n = n
        self.z = n - x - y + 1
        self.count = 0
        self.cache = {}
        self.cache_factorial = {}
        
    def calc(self):
        if self.z == 0:
            return self.simple_arrangements(self.x,self.y,self.n)
        if self.x + self.y == 3:
            return self.factorial(self.n-2)
        return (1.*self.shown()*self.sum_z(self.z,range(1,self.n-1),0)*
        self.factorial(self.z)*self.factorial(self.n-self.z-2)/
        self.factorial(self.n-2))
        
    def sum_z(self,z,m_range,subtractor):
        
        if z == 0:
            return 1
        
        key = "%i,%s,%i" %(z,str(m_range),subtractor)        
        
        if key not in self.cache:
            self.cache[key] = \
            self._sum_z(z,m_range,subtractor)
        return self.cache[key]
        
        
    def _sum_z(self,z,m_range,subtractor):
        sum = 0   
        for m in m_range:
            if m != subtractor:
                sum += m*self.sum_z(z-1,m_range,m)
        return sum
    
    def shown(self):
        return self._shown(self.x,self.y) + self._shown(self.y,self.x)
        
    def _shown(self,a,b):
        
        if b < 2:
            return 0
        
        if a > 1:
            c = self.factorial(a-1)*1.
            d = self.factorial(self.n-a-1)*1.
            term_a = self.factorial(self.n-2)/c/d
        else:
            term_a = 1
            
        if b > 2:
            
            c = self.factorial(self.n-a-1)*1.
            d = self.factorial(b-2)*1.
            e = self.factorial(self.n-a-b+1)*1.
            term_b = c/d/e
        else:
            term_b = 1
            
        return term_a*term_b
        
    def factorial(self,n):
        if n not in self.cache_factorial:
            self.cache_factorial[n] = self._factorial(n)
        return self.cache_factorial[n]
    
    def _factorial(self,n):
        if n == 0 or n == 1:
            return 1
        return n*self.factorial(n-1)
        
    def simple_arrangements(self,x,y,n):
        return self.factorial(n-1.)/self.factorial(x-1.)/self.factorial(y-1.)

